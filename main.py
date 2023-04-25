import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=english+to+amharic")

# wait = WebDriverWait(driver, 10)

search_source_lang = driver.find_element(By.ID, "tw-sl")
search_source_lang.click()

# source_lang = wait.until(EC.element_to_be_clickable((By.ID, "tw-sl")))
# source_lang.send_keys("Oromo")
# source_lang.send_keys(Keys.RETURN)
# time.sleep(2)

# search_target_lang = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@jsname='zumM6d']")))
# search_target_lang.click()

# target_langs = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[4]')))
# target_langs.send_keys(Keys.RETURN)
# time.sleep(2)

# search_target_lang = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button')))
# search_target_lang.click()

# df = pd.read_excel(
#     r"C:\Users\usr\OneDrive\Desktop\AI PROJECT\Data-Cleaner\language_dataset.xlsx")
# df = pd.read_excel(r"C:\Users\CBE\Desktop\AI Projects\Cleaning Datasets\language_dataset.xlsx")


# Find the first row where the "amh" column is empty
# start_index = df["amh"].isna().idxmax()

# Iterate over each row in the DataFrame
# for index, row in df.loc[start_index:].iterrows():
#     # Get the text to translate from the "orm" column
#     text_to_translate = row["orm"]

#     # Translate the text from Oromo to Amharic
#     oromo_lang = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')))
#     oromo_lang.send_keys(text_to_translate)

#     time.sleep(15)
#     # Write the translated text to the "amh" column
#     amharic_lang = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span')))
#     df.at[index, "amh"] = amharic_lang.text

#     # Write the updated DataFrame to the same Excel file
#     df.to_excel(
#         r"C:\Users\usr\OneDrive\Desktop\AI PROJECT\Data-Cleaner\language_dataset.xlsx", index=False)
#     # df.to_excel(r"C:\Users\CBE\Desktop\AI Projects\Cleaning Datasets\language_dataset.xlsx", index=False)

#     oromo_langs = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//*[@jsname='BJE2fc']")))
#     oromo_langs.clear()

#     print(index)
