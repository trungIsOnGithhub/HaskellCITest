import os
import urllib
import urllib2

def post_request(url, headers=None, data={}):
    request = urllib2.Request(url, headers=headers or {})
    data = urllib.urlencode(data).encode()
    try:
        with urllib2.urlopen(request, timeout=10, data=data) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")

def send_text_output(submission_data : Dict):
    output_url = os.environ.get('OUTPUT_API_URI')

    if output_url is None:
        raise Exception('Output URI is not provided')

    post_request(output_url, data=submission_data)

if __name__ == '__main__':
    send_text_output(sys.argv[0])
