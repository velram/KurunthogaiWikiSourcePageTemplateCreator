

def generate_wikisource_page_header(curr_pg_start_idx_start):

	if(curr_pg_start_idx_start <= 391):
		current_page_index_end=curr_pg_start_idx_start + 9
		previous_page_index_start=curr_pg_start_idx_start-10
		previous_page_index_end=curr_pg_start_idx_start-1
		next_page_index_start=curr_pg_start_idx_start+10
		next_page_index_end=next_page_index_start+9
		wikisource_page_header = ('{{தலை \n| தலைப்பு    = [[குறுந்தொகை]] '
			+str(curr_pg_start_idx_start)+'-'+str(current_page_index_end)+' \n'
			+'| எழுத்தாளர்   =  ' + '\n' +
			'| பாகம்  =  ' +
			'| முந்தியபக்கம் =  [[குறுந்தொகை '+str(previous_page_index_start)+' முதல் '+str(previous_page_index_end)+
			' முடிய|குறுந்தொகை '+str(previous_page_index_start)+'-'+str(previous_page_index_end)+']]' + '\n' +
			'| அடுத்தபக்கம்     = [[குறுந்தொகை '+str(next_page_index_start)+' முதல் '+str(next_page_index_end)+
			' முடிய|குறுந்தொகை '+str(next_page_index_start)+'-'+str(next_page_index_end)+']]' + '\n' +
			'| குறிப்புகள்    = ' + '\n' +
			'}}'
			)
		print("\n Page header is : \n" + wikisource_page_header)

	if(curr_pg_start_idx_start == 401):
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

if __name__ == '__main__':
	for index in range(151, 402, 10):
		print("Current index is : ", index)
		# wikisource_page_header = generate_wikisource_page_header(index)
		index = index + 10
