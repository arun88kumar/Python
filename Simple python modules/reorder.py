import pprint
def reorder(d):
	final_dict = dict();
	for key in d:
		#print final_dict;
		split_list = key.split('/')
		if len(split_list) > 1:
			if split_list[0] in final_dict.keys():
				value_dict = final_dict[split_list[0]]
				if type(value_dict) is str:
					final_dict[split_list[0]] = dict([(split_list[1],d[key])])
				else:
					value_dict[split_list[1]] = d[key]
					final_dict[split_list[0]] = value_dict
			else:
				final_dict[split_list[0]] = dict([(split_list[1],d[key])])
		else:
			if key in final_dict.keys():
				pass
			else:
				final_dict[key] = d[key]
				
	return final_dict
	
if __name__ == "__main__":
	dic = { "key1" : "value1",
			"key2/subkey1" : "value2",
			"key2/subkey2" : "value3",
			"key2" : "value4",
			"key3" : "value5",
			"key4" : "value6",
			"key5/subkey1" : "value7",
			"key6" : "value8",
			"key7/subkey1" : "value9",
			"key7/subkey2" : "value10",
			}
	pprint.pprint(reorder(dic))