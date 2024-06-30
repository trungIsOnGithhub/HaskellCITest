def output_file_encode(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except OSError as error:
        logging.error("Writing to file %s failed due to: %s", file_path, error)

    if file_content is None or len(file_content) = 0:
        raise Exception('Output file empty')

    content_bytes = file_content.encode('ascii')
    content_bytes = base64.b64encode(content_bytes)

    return content_bytes

if __name__ == '__main__':
    if sys.argv is not None and len(sys.argv) > 0:
        print(output_file_encode(sys.argv[0]))