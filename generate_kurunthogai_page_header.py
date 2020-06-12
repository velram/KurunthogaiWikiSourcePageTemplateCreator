import sys


def write_kurunthogai_page_header_to_file(kurunthogai_page_headers):
    orig_stdout = sys.stdout
    file_object = open('kurunthogai_page_headers.txt', 'w')
    sys.stdout = file_object
    for poem_page_header in kurunthogai_page_headers:
        print("\n\n" + poem_page_header)
    sys.stdout = orig_stdout
    file_object.close()


def generate_wikisource_page_header(curr_pg_start_idx_start):
    wikisource_page_header = None
    if curr_pg_start_idx_start <= 391:
        wikisource_page_header = get_wikisource_page_header(curr_pg_start_idx_start)

    if curr_pg_start_idx_start == 401:
        wikisource_page_header = get_final_poem_page_header(curr_pg_start_idx_start, wikisource_page_header)
    return wikisource_page_header


def get_wikisource_page_header(curr_pg_start_idx_start):
    current_page_index_end = curr_pg_start_idx_start + 9
    previous_page_index_start = curr_pg_start_idx_start - 10
    previous_page_index_end = curr_pg_start_idx_start - 1
    next_page_index_start = curr_pg_start_idx_start + 10
    next_page_index_end = next_page_index_start + 9
    wikisource_page_header = ('{{தலை \n| தலைப்பு = [[குறுந்தொகை]] '
                              + str(curr_pg_start_idx_start) + '-' + str(current_page_index_end) + ' \n'
                              + '| எழுத்தாளர் = ' + '\n' +
                              '| பாகம் = ' +
                              '| முந்தியபக்கம் = [[குறுந்தொகை ' + str(previous_page_index_start) + ' முதல் ' + str(
                previous_page_index_end) +
                              ' முடிய|குறுந்தொகை ' + str(previous_page_index_start) + '-' + str(
                previous_page_index_end) + ']]' + '\n' +
                              '| அடுத்தபக்கம் = [[குறுந்தொகை ' + str(next_page_index_start) + ' முதல் ' + str(
                next_page_index_end) +
                              ' முடிய|குறுந்தொகை ' + str(next_page_index_start) + '-' + str(
                next_page_index_end) + ']]' + '\n' +
                              '| குறிப்புகள் = ' + '\n' +
                              '}}'
                              )
    print("\n Page header is : \n" + wikisource_page_header)
    return wikisource_page_header


# Since Kurunthogai has only 401 poems. The last last page is 401.
# So, this code is to handle that edge case scenario.
def get_final_poem_page_header(curr_pg_start_idx_start, wikisource_page_header):
    previous_page_index_start = curr_pg_start_idx_start - 10
    previous_page_index_end = curr_pg_start_idx_start - 1
    wikisource_page_header = ('{{தலை \n| தலைப்பு    = [[குறுந்தொகை]] '
                              + str(curr_pg_start_idx_start) + ' \n'
                              + '| எழுத்தாளர்   =  ' + '\n' +
                              '| பாகம்  =  ' +
                              '| முந்தியபக்கம் =  [[குறுந்தொகை ' + str(previous_page_index_start) + ' முதல் ' + str(
                previous_page_index_end) +
                              ' முடிய|குறுந்தொகை ' + str(previous_page_index_start) + '-' + str(
                previous_page_index_end) + ']]' + '\n' +
                              '| குறிப்புகள்    = ' + '\n' +
                              '}}'
                              )
    return wikisource_page_header


def get_all_kurunthogai_page_headers():
    poem_page_headers = []
    for index in range(151, 402, 10):
        print("\n Current index is : ", index)
        poem_page_header = generate_wikisource_page_header(index)
        poem_page_headers.append(poem_page_header)
        index = index + 10
    print("\n\n All page headers : \n\n ", poem_page_headers)
    return poem_page_headers


if __name__ == '__main__':
    temp_headers = get_all_kurunthogai_page_headers()
    write_kurunthogai_page_header_to_file(temp_headers)
