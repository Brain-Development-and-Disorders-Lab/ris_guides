# Transferring Data

## Using `rclone`

[RClone](https://rclone.org/) is a command-line tool that can be used to copy files between different cloud storage applications.

### `rclone` Installation

Review the installation documentation [here](https://rclone.org/install/), but the general steps are as follows:

* **MacOS**: Install via Brew (`brew install rclone`), or install a pre-compiled version using the steps [here](https://rclone.org/install/#macos-precompiled).
* **Linux**: Install a pre-compiled version using the steps [here](https://rclone.org/install/#linux).
* **Windows**: Download a pre-compiled version from the page [here](https://rclone.org/install/#windows-precompiled).

### `rclone` Setup

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

### `rclone` Usage

> [!WARNING]
> During transfers to mounted network drives, the host PC connection must remain active, otherwise the transfer will fail.

To transfer from Box to a mounted network shared drive (i.e. RIS Storage), use the following command:

`rclone copy Box:<Source Directory> <Destination Directory> -v`

Where:

* Replace `<Source Directory>` with the path to the folder on Box, formatted : `Documents/folder_a/folder_b` etc.
* Replace `<Destination Directory>` with the path to the mounted network shared drive.

### `rclone` Examples

1. Copy directory contents from Box to a mounted RIS directory:

    `rclone copy Box:Documents/RClone_Test /Volumes/first.last.projects/Active/User/RClone_Test -v`

    *Note:* The `-v` option shows "verbose" output during the transfer to keep up with progress.

## Using `rsync`

[rsync](https://rsync.samba.org/) is a fast and versatile command-line tool for efficiently transferring and synchronizing files between directories or across networks.

### `rsync` Installation

Review the installation documentation [here](https://rsync.samba.org/), but the general steps are as follows:

* **MacOS**: Install via Brew (`brew install rsync`), or it comes pre-installed on most versions
* **Linux**: Install via package manager:
  * Ubuntu/Debian: `sudo apt-get install rsync`
  * Fedora: `sudo dnf install rsync`
  * CentOS/RHEL: `sudo yum install rsync`
* **Windows**: Install via:
  * WSL (Windows Subsystem for Linux): Use the Linux instructions above
  * Cygwin: Install through the Cygwin installer
  * Git Bash: Comes pre-installed

### `rsync` Usage

The basic syntax for `rsync` is:

`rsync [options] source destination`

Common options include:

* `-a`: Archive mode (recursive, preserve permissions, etc.)
* `-v`: Verbose output
* `-z`: Compress during transfer
* `--progress`: Show progress during transfer
* `--delete`: Remove files in destination that don't exist in source
* `--exclude`: Skip files matching pattern

> [!WARNING]
> Be careful with the `--delete` option as it will remove files in the destination that don't exist in the source. Always verify your paths and options before running rsync commands.

### `rsync` Examples

1. Local directory sync:

    ```bash
    rsync -avz /path/to/source/ /path/to/destination/
    ```

2. Remote sync over SSH:

    ```bash
    rsync -avz user@remote:/path/to/source/ /path/to/destination/
    ```

3. Sync with progress and exclude certain files:

    ```bash
    rsync -avz --progress --exclude '*.tmp' /path/to/source/ /path/to/destination/
    ```

4. Two-way sync (mirror):

    ```bash
    rsync -avz --delete /path/to/source/ /path/to/destination/
    ```

> [!NOTE]
> The trailing slash in source paths is important:
>
> * With trailing slash: contents of the directory are copied
> * Without trailing slash: the directory itself is copied
>
