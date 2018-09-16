# API References

## User
### Create User
> Make a unique user to manage multi-platform account.

#### Authentification
Token-Based authentification is required.

#### URL
> **POST** /user/create

#### Query String Parameters
Name | Type | Description
-----|------|------------
discord_id | integer | A discord id to register with
discord_name | string | A nickname of a specific discord user

#### Example Request & Response
- Case 1
    - Request
    ```sh
    curl -H 'Authentification: Bearer d7yA8hfT4OxgCq9q9qUHCrtXcyP5tZHn'
    -d '{"discord_id":"281729627003682818", "discord_name": "이은학"}'
    -X POST 'https://api.team-crescen.do/user/create'
    ```

    - Response
    ```json
    {
        "uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4",
        "discord_id": "281729627003682818",
        "discord_name": "이은학"
    }
    ```

---

### Get User info
> Get information of a specific user.

#### Authentification
Token-Based authentification is required.

#### URL
> **GET** /user/info/[uuid]

#### Query String Parameters
*None*

#### Example Request & Response
- Case 1
    - Request
    ```sh
    curl -H 'Authentification: Bearer d7yA8hfT4OxgCq9q9qUHCrtXcyP5tZHn'
    -X POST 'https://api.team-crescen.do/user/info/48515667-a305-6f5e-9e4f-88016f5a63b4'
    ```

    - Response
    ```json
    {
        "uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4",
        "discord_id": "281729627003682818",
        "discord_name": "이은학"
    }
    ```

---

### Search Users
> Search users with given metadata.

#### Authentification
Token-Based authentification is required.

#### URL
> **GET** /user/search

#### Query String Parameters
*None*

#### Example Request & Response
- Case 1
    - Request
    ```sh
    curl -H 'Authentification: Bearer d7yA8hfT4OxgCq9q9qUHCrtXcyP5tZHn'
    -d '{"uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4"}'
    -X POST 'https://api.team-crescen.do/user/search'
    ```

    - Response
    ```json
    {
        "resultCount": 1,
        "result": [
            {
                "uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4",
                "discord_id": "281729627003682818",
                "discord_name": "이은학"
            }
        ]
    }
    ```

- Case 2
    - Request
    ```sh
    curl -H 'Authentification: Bearer d7yA8hfT4OxgCq9q9qUHCrtXcyP5tZHn'
    -d '{"discord_name": "이은학"}'
    -X POST 'https://api.team-crescen.do/user/search'
    ```

    - Response
    ```json
    {
        "resultCount": 2,
        "result": [
            {
                "uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4",
                "discord_id": "281729627003682818",
                "discord_name": "이은학"
            },
            {
                "uuid": "b040f925-516f-5445-c60a-92a295fe0730",
                "discord_id": "481124253937303585",
                "discord_name": "이은학"
            }
        ]
    }
    ```

## Point
### Fetch Point Data of a Specific User
> Fetch point data of a specific user by his/her uuid.

#### Authentification
Token-Based authentification is required.

#### URL
> **GET** /points/info/[uuid]

#### Query String Parameters
Name | Type | Description
-----|------|------------
uuid | UUID | UUID of a specific user to look up

#### Example Request & Response
- Case 1
    - Request
    ```sh
    curl -H 'Authentification: Bearer d7yA8hfT4OxgCq9q9qUHCrtXcyP5tZHn'
    -X GET 'https://api.team-crescen.do/points/info/48515667-a305-6f5e-9e4f-88016f5a63b4'
    ```

    - Response
    ```json
    {
        "uuid": "48515667-a305-6f5e-9e4f-88016f5a63b4",
        "point": 231000
    }
    ```

---
