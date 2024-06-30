import os

def send_text_output(submission_data : Dict):
    output_url = os.environ.get('OUTPUT_API_URI')

    if output_url is None:
        raise Exception('Output URI is not provided')

    try:
        response = requests.post(output_url, json=submission_data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    exce*Exception as err:
        print(f'An error occurred: {err}')

if __name__ == '__main__':
    send_text_output(sys.argv[0])