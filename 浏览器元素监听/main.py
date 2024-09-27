from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import subprocess

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")

# 连接到已经打开的Chrome浏览器
driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)

# 指定的元素选择器 (根据你的实际情况修改)
element_selector = 'your-element-selector'
expected_value = 'your-expected-value'

while True:
    try:
        # 刷新页面
        driver.refresh()
        time.sleep(2)
        # 查找元素
        element = driver.find_element_by_css_selector(element_selector)
        
        # 获取元素的值 (根据你的实际情况修改)
        element_value = element.text if element else None
        
        # 检查元素值是否为指定值
        if element_value == expected_value:
            # 调用cmd命令发送通知邮件
            cmd = f'notify "Element value is {expected_value}" "Notification Title"'
            subprocess.run(cmd, shell=True)
            break
        
    except Exception as e:
        print(f"Error: {e}")
    
    # 等待一段时间后重新检查 (例如每5秒检查一次)
    time.sleep(5)

# 关闭浏览器
driver.quit()