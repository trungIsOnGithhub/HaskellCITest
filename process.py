import os
import base64
import json

from contents import driver_code, utilities_code
from output import

def exercise_1_input_prepare(input_string, file_path):
    number_str_list = input_string[1:][:-1].split(',')

    file = open(file_path, 'w')

    for number_str in number_str_list:
        file.write(number_str + ' ')

def exercise_2_input_prepare(input_string, file_path):
    number_str_list = input_string.split(',')

    file = open(file_path, 'w')

    for number_str in number_str_list:
        file.write(number_str + ' ')

def get_json_input_encoded():
	return '''
        {
            "ex1": [
                {"id": "ex1.1", "input":"WzgsOCw4LDgsOCw4XQ=="},
                {"id": "ex1.2", "input":"Wy05LC05LC05LC05XQ=="},
                {"id": "ex1.3", "input":"WzYsLTgsOSwtNl0="}
            ],
            "ex2": [
                {"id": "ex2.1", "input":"MiwyMDIw"},
                {"id": "ex2.2", "input":"NSwyMDE3"}        
            ]
        }
    '''

if __name__ == '__main__':
    temp_input_file_path = './in.txt'
    exercise_ids = ['ex1', 'ex2']
    output = {}

    sample_json_input_string = get_json_input_encoded()
    sample_json_input_parsed = json.loads(sample_json_input_string)

    print(sample_json_input_parsed)

    for attr in exercise_ids:
        # print(attr)
        test_info = sample_json_input_parsed[attr]

        # print(test_info)

        if test_info is None:
            raise Exception('Test Not Existed!!')

        # print(exercise_tests)
        # print(type(exercise_tests))
        source_file_path = './' + attr + '/' + attr + '.hs'
        if not os.path.isdir(attr) or not os.path.isfile(source_file_path):
            raise Exception('Test Directory or File Not Existed!! Invalid Format!!')

        file = open(source_file_path, 'a')

        # print(source_file_path)
        # print(attr, type(attr))
        # print(contents.driver_code[attr])

        file.write(contents.utilities_code)
        file.write(contents.driver_code[attr]['input'])
        file.write(contents.driver_code[attr]['solution'])
        file.write(contents.driver_code[attr]['output'])

        output_list = []
        for test in test_info:
            input_encoded_bytes = test['input'].encode('ascii')
            input_string_bytes = base64.b64decode(input_encoded_bytes)
            input_string = input_string_bytes.decode('ascii')

            # print('hijilj  '+input_string)
            # print(type(input_string))

            if attr == 'ex1':
                exercise_1_input_prepare(input_string, temp_input_file_path)
            elif attr == 'ex2':
                exercise_2_input_prepare(input_string, temp_input_file_path)
            # contents.driver_code[attr]['input_prepare'](input_string, "./in.txt")

            status = os.system('ghc ' + source_file_path)
            if status != 0:
                raise Exception('Cannot Compile Haskell Source')
            status = os.system(f'./{attr}/{attr}')
            if status != 0:
                raise Exception('Cannot Execute Haskell Binaries')

            this_test_result = {}
            this_test_result['id'] = test['id']
            this_test_result['output'] = output_prepare('out.txt')

            output_list.append(this_test_result)

        output[attr] = output_list

    # print(output)