*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${BROWSER}    edge
${URL}    https://chiangmaiarea1-server.web.app/
${WELECOME}    https://chiangmaiarea1-server.web.app/#/News

*** Test Cases ***  # Case ที่จะทำ Test
Open Website And Test Login  # TestCase 1
    Open Website To Login Page  #เปิด Open Website To Login Page ใน Keywords (การทำงานเเบบ chian function)
    Input Username    admin     # ทำ Keywords ต่อไปนี้
    Input Password   ict111213ict  # ทำ Keywords ต่อไปนี้
    Submit Form
    Location Should Be  ${WELECOME} 
    [Teardown]   Close Browser

*** Keywords ***
Open Website To Login Page  # Keywords หรือ จะเรียกว่า function ที่ถูกจะถูกเปิด ต่อจากการทำ ใน Test Cases
  Open Browser  ${URL}    ${BROWSER}
  Maximize Browser Window
  Set Selenium Speed    1

Input Username
    [Arguments]  ${username}
    Input Text    xpath://input[@placeholder='Username']   ${username}
Input Password
    [Arguments]  ${password}
    Input Text    xpath://input[@placeholder='Password']   ${password}


Submit Form
  Click Button   xpath://input[@type='submit' and @value='Login']







  
   