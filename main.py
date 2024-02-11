class InvalidPageRangeError(Exception):
    def __init__(self, msg):
        self.msg = msg


def validate_page_range(start_page, end_page):
    if start_page > end_page:
        raise InvalidPageRangeError('The starting page should be lesser than the end page!')
    else:
        print('Fetching page data.....')


try:
    import pyttsx3, PyPDF2
except ImportError as e:
    e_str = str(e)
    print(f'{e_str}. Please install it using "pip install {e_str[17:]}".')
else:
    file = input("Enter the file name: ")
    try:
        book = open(file, 'rb')
    except FileNotFoundError as e:
        print('File you provided is not available!')
    except OSError as e:
        print('Please Enter correct File name')
    else:
        pdfReader = PyPDF2.PdfReader(book)
        print(f'The total number of pages are : {len(pdfReader.pages)}')
        try:
            startPageNo, endPageNo = eval(input("Enter the page range (start,end): "))
            try:
                validate_page_range(startPageNo, endPageNo)
            except InvalidPageRangeError as e:
                print(e)
        except SyntaxError as e:
            print('Please enter page range in the given format')
        except ValueError as e:
            print('Please Enter the values correctly!')
        except TypeError as e:
            print('Please Enter the page range in the given format!')
        else:
            for num in range(startPageNo-1, endPageNo):
                try:
                    pageToBeRead = pdfReader.pages[num]
                except IndexError as e:
                    print('Please Enter Valid Page Number!')
                    break
                else:
                    print(f'Reading page {num + 1}')
                    text = pageToBeRead.extract_text()
                    speaker = pyttsx3.init()
                    speaker.say(text)
                    speaker.runAndWait()
                print('Reading completed!')
        finally:
            book.close()