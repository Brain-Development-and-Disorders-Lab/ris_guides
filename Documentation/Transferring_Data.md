# Transferring Data

## Using `rclone`

[RClone](https://rclone.org/) is a command-line tool that can be used to copy files between different cloud storage applications.

### Installation

Review the installation documentation [here](https://rclone.org/install/), but the general steps are as follows:

* **MacOS**: Install via Brew (`brew install rclone`), or install a pre-compiled version using the steps [here](https://rclone.org/install/#macos-precompiled).
* **Linux**: Install a pre-compiled version using the steps [here](https://rclone.org/install/#linux).
* **Windows**: Download a pre-compiled version from the page [here](https://rclone.org/install/#windows-precompiled).

### Setup

After installing the `rclone` application, run the following command to configure a "remote":

`rclone config`

This will lead to the following steps:

1. Name the remote `Box`:

    ```text
    No remotes found, make a new one?
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> Box
    ```

2. Select Box from the list of types, either entering the number or the value `box`:

    ```text
    Type of storage to configure.
    Choose a number from below, or type in your own value
    [snip]
    XX / Box
      \ "box"
    [snip]
    Storage> box
    ```

3. Leave the `Client Id` blank:

    ```text
    Box App Client Id - leave blank normally.
    client_id>
    ```

4. Leave the `Client Secret` blank:

    ```text
    Box App Client Secret - leave blank normally.
    client_secret>
    ```

5. Leave the `config.json` location blank:

    ```text
    Box App config.json location
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    box_config_file>
    ```

6. Leave the `Primary Access Token` blank:

    ```text
    Box App Primary Access Token
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    access_token>
    ```

7. Select `1` for `rclone` to act as a "user":

    ```text
    Enter a string value. Press Enter for the default ("user").
    Choose a number from below, or type in your own value
    1 / Rclone should act on behalf of a user
      \ "user"
    2 / Rclone should act on behalf of a service account
      \ "enterprise"
    box_sub_type>
    ```

8. If you are using a desktop or laptop, select `y` for `rclone` to open a browser for authentication:

    ```text
    Remote config
    Use web browser to automatically authenticate rclone with remote?
    * Say Y if the machine running rclone has a web browser you can use
    * Say N if running rclone on a (remote) machine without web browser access
    If not sure try Y. If Y failed, try N.
    y) Yes
    n) No
    y/n> y
    If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=XXXXXXXXXXXXXXXXXXXXXX
    Log in and authorize rclone for access
    Waiting for code...
    Got code
    Configuration complete.
    ```

9. Select `y` to save this new remote:

    ```text
    Options:
    - type: box
    - client_id:
    - client_secret:
    - token: {"access_token":"XXX","token_type":"bearer","refresh_token":"XXX","expiry":"XXX"}
    Keep this "remote" remote?
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    ```

To test that setup has worked correctly, run the following command:

`rclone lsd Box:`

If successful, a list of all directories in your Box account should appear similar to below:

```output
  -1 2022-12-06 15:06:53        -1 Shared ****
  -1 2025-03-24 15:53:02        -1 Documents
  -1 2024-03-15 09:09:43        -1 **** Collaboration (WashU, ****) ****
  -1 2024-05-31 09:54:35        -1 Microsoft Teams Chat Files
  -1 2025-03-24 14:25:33        -1 Microsoft Teams Folder
  -1 2025-03-19 13:48:36        -1 Talks
```

### Usage

> [!WARNING]
> During transfers to mounted network drives, the host PC connection must remain active, otherwise the transfer will fail.

To transfer from Box to a mounted network shared drive (i.e. RIS Storage), use the following command:

`rclone copy Box:<Source Directory> <Destination Directory> -v`

Where:

* Replace `<Source Directory>` with the path to the folder on Box, formatted : `Documents/folder_a/folder_b` etc.
* Replace `<Destination Directory>` with the path to the mounted network shared drive.

Example:

`rclone copy Box:Documents/RClone_Test /Volumes/first.last.projects/Active/User/RClone_Test -v`

Note: The `-v` option shows "verbose" output during the transfer to keep up with progress.
