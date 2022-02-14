from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://danmarshall.github.io/google-font-to-svg-path/?font-select=ABeeZee&font-variant=regular&input-union=false&input-filled=true&input-kerning=true&input-separate=false&input-text=Idontknow&input-bezier-accuracy=&dxf-units=cm&input-size=100')
driver.implicitly_wait(245)

result = driver.page_source
print(result)