from docutils.core import publish_string
from sys import argv
from webbrowser import open as browser_open

TEMPLATE_CONTENTS = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{filename}</title>
        <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            {file_contents}
        </div>
  </body>
</html>
"""


def bootstrap_rest(filenames):
    if len(argv) < 2:
        raise TypeError('Needs at least one argument.')

    file_contents = ''
    for filename in argv[1:]:
        with open(filename) as file:
            file_contents += publish_string(file.read(), writer_name='html')

    return TEMPLATE_CONTENTS.format(
        filename=filename,
        file_contents=file_contents,
    )



if __name__=='__main__':
    if len(argv) < 2:
        raise TypeError('Needs at least one argument.')

    output_filename = "{}.html".format(argv[1])
    with open(output_filename, 'w') as output_file:
        output_content = bootstrap_rest(argv[1:])
        output_file.write(output_content)

    browser_open(output_filename)
