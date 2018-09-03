#Team Crescendo API Documentation

## Users
### User Object
| Name | Type | Length | Description |
|:----:|:----:|:------:|:------------|
| uuid | UUID | 36 | Unique User id (managed by Team Crescendo) <br/>_ex)_ abcd1234-ab12-cd34-ef56-abcdef123456 |
| discord | VARCHAR | 18 | Discord User ID (managed by Discord)<br />_ex)_ 281729627003682818 |
| twitch | VARCHAR | 9 | Twitch User ID (managed by Twitch)<br />_ex)_ 147108421 |

### Platform Reference
#### Discord
| Field Name | Type | Length | Description |
|:----------:|:----:|:------:|:------------|
| did | VARCHAR | 18 | Discord User ID _(referenced: users.discord)_|
| email | VARCHAR | 100 | User email from Discord OAuth2 Authorization |
| username | VARCHAR | 50 | Discord Username |

#### Twitch
| Field Name | Type | Length | Description |
|:----------:|:----:|:------:|:------------|
| tid | VARCHAR | 9 | Twitch User ID _(referenced: users.twitch)_|
| uid | VARCHAR | 30 | Twitch User Login ID|
| email | VARCHAR | 100 | User email from Twitch OAuth2 Authorization |
| username | VARCHAR | 50 | Twitch Display Name |


### Create new user
- Reqest
`POST /users/create`

    - Header

    ```markdown
    Authorization: <id>:<token>
    ```

    - Parameters

    | Param Name | Required | Description |
    |:----------:|:--------:|:------------|
    | platform | **YES** | Platform of the registration |
    | email | _Optional_ | |
    | username | _Optional_ | |
    | login_id | _Optional_, _Occational_ | **Only used in twitch user registration** <br /> Twitch Login id |

    - Example

    ```json
    {
        "platform": "discord",
        "": ""
    }
    ```

- Response
    - Body
        - Success
        ```json
        {
            "code": 0,
            "message": "",
            "uuid": "abcd1234-ab12-cd34-ef56-abcdef123456"
        }
        ```

        - Fail
        ```json
        {
            "code": code,
            "message": "message of the error",
            "uuid": ""
        }
        ```

        - Response Code

        | Code | Error |
        |:----:|:------|
        | 0 | Success. No error |
        | 301 | ID passed is already registered |
        | 302 | 
