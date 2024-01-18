


# from autoscraper import AutoScraper

# data = [
#     ('https://www.boohoo.com/prince-embroidered-ribbed-vest-top/GZZ78560.html?color=173', ['£9.00']),
#     ('https://www.boohoo.com/prince-tricot-straight-leg-jogger/GZZ78569.html?color=157', ['£16.00']),
#     ('https://www.boohoo.com/brushed-rib-2-in-1-high-neck-dress-/GZZ75645.html', ['£20.00']),
#     ('https://www.boohoo.com/rouched-detail-ribbed-mini-bodycon-dress/GZZ55232.html?color=165', ['£15.00']),
#     ('https://www.boohoo.com/boxy-fit-acid-wash-denim-zip-through-hoodie/BMM68073.html', ['£21.00']),

#     # shein
#     ('https://www.shein.co.uk/Men-Letter-Graphic-Kangaroo-Pocket-Drawstring-Thermal-Lined-Hoodie-p-24688682.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_4%60ps%3D4_4%60jc%3Dreal_2026&src_module=Women&src_tab_page_id=page_home1705542919383&mallCode=1&imgRatio=3-4', ['£5.26']),
#     ('https://www.shein.co.uk/Men-s-Beach-Shorts-With-Coconut-Tree-Print-And-Drawstring-Waist-p-28850838.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_4%60ps%3D4_4%60jc%3Dreal_2026&src_module=Women&src_tab_page_id=page_home1705542919383&mallCode=1&imgRatio=3-4', ['£11.99']),

#     # temu
#     ('https://www.temu.com/uk/sequin-off-shoulder-drawstring-shirt-boho-long-sleeve-pullover-shirt-for-spring-fall-womens-clothing-g-601099531055671.html?top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F25e99b91b1f1d94c1d9e2bcc67f48ae6.jpg&spec_id=2001&spec_gallery_id=1218&refer_page_sn=15498&refer_source=0&freesia_scene=2&_oak_freesia_scene=2&_oak_rec_ext_1=MTE2OQ&_oak_gallery_order=1592752215%2C1721258538%2C359382274%2C1257743989&spec_ids=2001&refer_page_el_sn=223143&_x_vst_scene=adg&_x_ads_sub_channel=search&_x_ads_channel=bing&_x_ads_account=176202190&_x_ads_set=519193183&_x_ads_id=1316117718217619&_x_ads_creative_id=82257583982288&_x_ns_source=s&_x_ns_msclkid=fa4b4b6bd5af162d4b3f2ec3aaab268a&_x_ns_match_type=e&_x_ns_bid_match_type=be&_x_ns_query=boohoo&_x_ns_keyword=.%20boohoo&_x_ns_device=c&_x_ns_targetid=kwd-82258273365826%3Aloc-188&_x_ns_extensionid=&refer_page_name=kuiper&refer_page_id=15498_1705543074412_0bz81fv0ux&_x_sessn_id=qlf3tlqhds', ['£11.69']),
#     ('https://www.temu.com/uk/boho-two-piece-set-short-sleeve-crop-top-high-waist-wide-leg-pants-outfits-womens-clothing-g-601099514223019.html?top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F22d7374202b907804fc1e1cc517f9558.jpg&spec_id=16066&spec_gallery_id=166&refer_page_sn=15498&refer_source=0&freesia_scene=2&_oak_freesia_scene=2&_oak_rec_ext_1=MTQ5OA&_oak_gallery_order=1667989475%2C1983396570%2C1389123992%2C795356896%2C1749134992&spec_ids=16066%2C2001%2C16057&refer_page_el_sn=223143&_x_vst_scene=adg&_x_ads_sub_channel=search&_x_ads_channel=bing&_x_ads_account=176202190&_x_ads_set=519193183&_x_ads_id=1316117718217619&_x_ads_creative_id=82257583982288&_x_ns_source=s&_x_ns_msclkid=fa4b4b6bd5af162d4b3f2ec3aaab268a&_x_ns_match_type=e&_x_ns_bid_match_type=be&_x_ns_query=boohoo&_x_ns_keyword=.%20boohoo&_x_ns_device=c&_x_ns_targetid=kwd-82258273365826%3Aloc-188&_x_ns_extensionid=&refer_page_name=kuiper&refer_page_id=15498_1705543074412_0bz81fv0ux&_x_sessn_id=qlf3tlqhds', ['£11.49']),
# ]

# scraper = AutoScraper()
# for url, wanted_list in data:
#     result = scraper.build(url=url, wanted_list=wanted_list, update=True)
#     print(scraper.get_result_exact(url, grouped=True))

# scraper.keep_rules(['rule_ojlp'])
# ourpredicted_result = scraper.get_result_exact('https://newbiestore.com/products/261966?nosto=productcategory-nosto-2-fallback-nosto-1', group_by_alias=True)
# print('*************************\n')
# print(ourpredicted_result)



import re
# import requests
# from bs4 import BeautifulSoup
# import json

# def smart_scrape_data(keywords, websites):
#     results = []

#     for website in websites:
#         try:
#             # Send an HTTP request and get the HTML content
#             response = requests.get(website)
#             html_content = response.text

#             # Parse the HTML content with BeautifulSoup
#             soup = BeautifulSoup(html_content, 'html.parser')

#             # Extract data based on user-provided keywords
#             website_results = {}

#             for keyword in keywords:
#                 # Search for the keyword in both text content and HTML attributes
#                 text_matches = soup.find_all(string=re.compile(f'.*{keyword}.*', re.I))
#                 attr_matches = soup.find_all(attrs={'class': re.compile(f'.*{keyword}.*', re.I)})

#                 # Combine text and attribute matches
#                 matches = text_matches + attr_matches

#                 # Extract data from parent elements for well-structured information
#                 data = [str(match.find_parent().get_text(strip=True)) for match in matches]

#                 # Use class names as labels
#                 label = f"{keyword}_labels"
#                 website_results[label] = data

#             results.append({website: website_results})

#         except Exception as e:
#             print(f"Error scraping {website}: {str(e)}")

#     return results

# # Example usage
# user_keywords = ['name', 'images', 'price']
# user_websites = ['https://www.boohoo.com/womens/tops', 'https://www.boohoo.com/womens/dresses']

# scraped_data = smart_scrape_data(user_keywords, user_websites)

# # Print or process the scraped data
# for website_data in scraped_data:
#     for website, results in website_data.items():
#         print(f"Results for {website}:")
#         # print(json.dumps(results, indent=2))
#         # write to file
#         with open('data.json', 'w') as outfile:
#             json.dump(results, outfile)


# # Path: dump.py
import requests
# from bs4 import BeautifulSoup
# from collections import Counter

# def find_repeating_structure(url):
#     try:
#         # Send an HTTP request and get the HTML content
#         response = requests.get(url)
#         soup = response.text

#         # Parse the HTML content with BeautifulSoup
#         # soup = BeautifulSoup(html_content, 'html.parser')

#         # Find all divs and create a representation of their structure
#         div_structures = []

#         for div in soup.find_all('div'):
#             structure = []
#             for tag in div.find_all(recursive=False):
#                 structure.append(tag.name)
#             div_structures.append(tuple(structure))

#         # Find the most common structure
#         common_structure, _ = Counter(div_structures).most_common(1)[0]

#         # Find the first div with the most common structure
#         example_div = soup.find(lambda tag: tuple(tag.find_all(recursive=False)) == common_structure)

#         # Return the example div
#         return example_div

#     except Exception as e:
#         print(f"Error finding repeating structure on {url}: {str(e)}")
#         return None

# # Example usage
# url_to_scrape = 'https://www.boohoo.com/womens/tops'
# repeating_structure = find_repeating_structure(url_to_scrape)

# if repeating_structure:
#     print(f"Repeating structure found on {url_to_scrape}:\n{repeating_structure}")
# else:
#     print(f"No repeating structure found on {url_to_scrape}")
