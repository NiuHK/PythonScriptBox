from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

# 连接到已经运行的Chrome实例
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9223"
driver = webdriver.Chrome(options=chrome_options)

# 获取所有打开的标签页句柄
handles = driver.window_handles
# 列出所有标签页的编号和名称
print("当前打开的标签页信息:")
tab_info = []
for index, handle in enumerate(handles):
    driver.switch_to.window(handle)
    title = driver.title  # 获取标签页标题
    tab_info.append((index, title, handle))
    print(f" {index}:{title}")
    
    

# 让用户输入要切换到的标签页编号
tab_index = int(input("请输入要切换到的标签页编号: "))

# 切换到指定标签页
driver.switch_to.window(handles[tab_index])
print(f"已切换到标签页 {tab_index}: 标题 - '{driver.title}'")



def send_keys_with_shift(driver, text_value):
    actions = ActionChains(driver)
    shift_chars = {
        '#': '3',
        '%': '5',
        '^': '6',
        '&': '7',
        '*': '8',
        '(': '9',
        ')': '0',
        '_': '-',
        '+': '=',
        '{': '[',
        '}': ']',
        ':': ';',
        '"': "'",
        '<': ',',
        '>': '.',
        '?': '/',
        '|': '\\'
    }
    for char in text_value:
        if char in shift_chars:
            actions.key_down(Keys.SHIFT)
            time.sleep(0.1)
            actions.send_keys(shift_chars[char])
            time.sleep(0.1)
            actions.key_up(Keys.SHIFT)
            
        else:
            actions.send_keys(char)
    actions.send_keys(Keys.ENTER)  # 模拟回车键
    actions.perform()  # 执行操作链



while True:
    input_text = input()
    send_keys_with_shift(driver, input_text)