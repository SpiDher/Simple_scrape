from lxml import html
import requests
import os
import json
filename= os.path.join('data.json')
page_number = 1

params = {
    'page': f'{page_number}',
}


questions_dict = {}

headers = {
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=0, i',
}
url= 'https://myschool.ng/classroom/english-language'
response = requests.get(url, headers=headers, params=params)

tree = html.fromstring(response.content)

questions = len(tree.xpath('//div[@id="question-listing"]/div[contains(@class, "question-item")]'))

for i in range(questions):
    print("\n" + "=" * 100 + "\n" + "=" * 100 + "\n")
    question = tree.xpath(f'(//div[@id="question-listing"]/div[contains(@class, "question-item")])[{i + 1}]/div[contains(@class, "media-body")]//div')[0].text_content()
    options = tree.xpath(f'(//div[@id="question-listing"]/div[contains(@class, "question-item")])[{i + 1}]/div[contains(@class, "media-body")]//ul')[0].text_content()
    q_no = tree.xpath(f'(//div[@id="question-listing"]/div[contains(@class, "question-item")])[{i + 1}]/div[contains(@class, "question_sn")]/text()')[0]
    ans_link = tree.xpath(f'(//div[@id="question-listing"]/div[contains(@class, "question-item")])[{i + 1}]/div[contains(@class, "media-body")]//a')[0].attrib['href']
    cleaned_options = "\n".join([line.strip() for line in options.splitlines() if line.strip()])
    questions_dict[q_no] = {
        'question': question,
        'options': cleaned_options,
        'ans_link': ans_link,
    }
    print(f"Question {q_no}: {question}\n\n{cleaned_options}")


input(f"\n\nRetrieving answers for page {page_number}. Press Enter to continue...")

for q_no in questions_dict:
    ans_url = questions_dict[q_no]['ans_link']
    try:
        ans_response = requests.get(ans_url, headers=headers)
        ans_tree = html.fromstring(ans_response.content)
        ans = ans_tree.xpath('//h5[contains(text(), "Correct Answer:")]/text()')
        questions_dict[q_no]['answer'] = ans
        del questions_dict[q_no]['ans_link']
        print(f"Answer for question {q_no} retrieved successfully.")
    except Exception as e:
        print(f"Failed to retrieve answer for question {q_no}. Error: {e}")


os.system('clear')

print("\n\n" + "=" * 100 + "\n" + "=" * 100 + "\n")
if os.path.exist(filename):
    with open(filename,'r')as file:
        data=json.load(file)
else:
    data =[]
for q_no in questions_dict:
    collection = {'qst':{questions_dict[q_no]['question']},
    'opt':questions_dict[q_no]['options'],
    'ans':questions_dict[q_no]['answer']
    }
    data.append(collection)
    print(f"Question {q_no}: {questions_dict[q_no]['question']}\n\n{questions_dict[q_no]['options']}\n\nAnswer: {questions_dict[q_no]['answer']}\n\n" + "=" * 100 + "\n" + "=" * 100 + "\n")

with open(filename,'w') as file:
    json.dump(data,file,indent=4)