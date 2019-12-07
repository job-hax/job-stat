import json


def employee_in(data, comp):
    comp = comp.lower()
    employees = []
    for line in data:
        job = ' '.join(line["current_job"]).lower()
        if comp in job:
            employees.append(line)

    return employees


def extract_top_skills(data):
    res = []
    for line in data:
        A = []
        for k, val in line.items():
            if k == 'name':
                if "," in val:
                    val = val[:val.index(",")]
                A.append(val)
            elif k == 'top_skills':
                A.extend(val[:3])

        if len(A) == 4:
            res.append(A)

    return res  # list of list


def generate_train_data(data, comp):
    # employees hired by comp will be labelled 'Matched', else 'Unmatched'
    company = comp.lower()
    names = [emp['name'] for emp in employee_in(data, company)]
    res = []
    line = ''
    with open('train.csv', 'w') as f:
        for sbj in extract_top_skills(data):
            if sbj[0] in names:
                # sbj.append("Matched\n")
                line = ','.join(sbj) + ",Matched\n"
            else:
                # sbj.append("Unmatched\n")
                line = ','.join(sbj) + ",Unmatched\n"
            # res.append(sbj)

            f.write(line)


def generate_test_data(data, comp):
    data = data[len(data)-10:]
    line = ''
    with open('test.csv', 'w') as f:
        for sbj in extract_top_skills(data):
            line = ','.join(sbj) + ",Applied\n"
            f.write(line)


if __name__ == "__main__":
    company = 'Google'
    print(f"Generate train or test data for {company}")
    
    # train_test = input('Generate train or test data (train or test) ')
    train_test = 'test'
    with open('data.json', 'r') as json_file:
        data = [json.loads(x) for x in json_file.readlines()]
    
    if train_test == 'train':
        generate_train_data(data, company)
    elif train_test == 'test':
        generate_test_data(data, company)
    else:
        print("Invalid input")
