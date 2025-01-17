import openreview

# read the json file of yourself
import json
with open('username_passwd.json', 'r') as f:
    jsondata = json.load(f)
username = jsondata['username']
password = jsondata['password']

# read conference full name
with open('conferencefullname.json', 'r') as f:
    conference_full_name = json.load(f)


# 适用于 API V2 的客户端实例
client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username= username, password= password
)


def get_submissions(client, venue_id, status='all'):
    # Retrieve the venue group information
    venue_group = client.get_group(venue_id)
    
    # Define the mapping of status to the respective content field
    status_mapping = {
        "all": venue_group.content['submission_name']['value'],
        "accepted": venue_group.id,  # Assuming 'accepted' status doesn't have a direct field
        "under_review": venue_group.content['submission_venue_id']['value'],
        "withdrawn": venue_group.content['withdrawn_venue_id']['value'],
        "desk_rejected": venue_group.content['desk_rejected_venue_id']['value']
    }

    # Fetch the corresponding submission invitation or venue ID
    if status in status_mapping:
        if status == "all":
            # Return all submissions regardless of their status
            return client.get_all_notes(invitation=f'{venue_id}/-/{status_mapping[status]}')
        
        # For all other statuses, use the content field 'venueid'
        return client.get_all_notes(content={'venueid': status_mapping[status]})
    
    raise ValueError(f"Invalid status: {status}. Valid options are: {list(status_mapping.keys())}")


from datetime import datetime

def extract_submission_info(submission):
    # Helper function to convert timestamps to datetime
    def convert_timestamp_to_date(timestamp):
        return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d') if timestamp else None

    # Extract the required information
    submission_info = {
        'id': submission.id,
        'title': submission.content['title']['value'],
        'authors': submission.content['authors']['value'],
        'abstract': submission.content['abstract']['value'],
        'keywords': submission.content['keywords']['value'],
        'primary_area': submission.content['primary_area']['value'],
        'TLDR': submission.content['TLDR']['value'] if 'TLDR' in submission.content else "",
        'creation_date': convert_timestamp_to_date(submission.cdate),
        'original_date': convert_timestamp_to_date(submission.odate),
        'modification_date': convert_timestamp_to_date(submission.mdate),
        'forum_link': f"https://openreview.net/forum?id={submission.id}",
        'pdf_link': f"https://openreview.net/pdf?id={submission.id}"
    }
    return submission_info


# write refer to RIS format
def write_to_ris(submissions, output_file, year, conference_name):
    with open(output_file, 'w', encoding='utf-8') as f:
        for submission in submissions:
            submission_infor = extract_submission_info(submission)
            # Write RIS header
            f.write("TY  - CONF\n") # conferenece paper:CONF, journal:JOUR, book:BOOK, thesis:THES
 
            # Title
            title = submission_infor['title']
            f.write(f"TI  - {title}\n")
 
            # Authors
            authors = ', '.join(submission_infor['authors'])
            f.write(f"AU  - {authors}\n")
 
            # Year
            f.write(f"PY  - {year}\n")
 
            # conference
            name = conference_full_name[conference_name]
            f.write(f"SO  - {name}\n")

            # Abstract
            abstract = submission_infor['abstract']
            f.write(f"AB  - {abstract}\n")

            # PDF link
            pdf_link = submission_infor['pdf_link']
            f.write(f"UR  - {pdf_link}\n")

            # End of record
            f.write("ER  - \n\n")
    print(f"Converted {len(submissions)} records to RIS format and saved to {output_file}")



if __name__ == "__main__":

    # customize the venue_id and status
    venue_id = 'ICLR.cc/2025/Conference' # ICLR.cc/2023/Conference
    status = 'all'  # accepted, under-review, all, under_review, desk_rejected.

    year = venue_id.split('/')[1]
    conference_name = venue_id.split('/')[0].split('.')[0]
    print(conference_full_name[conference_name])
    output_file = f"{conference_name}-{year}-{status}.ris"

    submissions = get_submissions(client, venue_id, status)
    print("the number of paper is:{}".format(len(submissions)))
    write_to_ris(submissions, output_file, year, conference_name)

