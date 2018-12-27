# Autofill text with a 2FA code for use in VPN

### Requirements:

1. [Docker](https://www.docker.com/get-started).
2. `mi-<your-name>.ovpn` file from admin (check your email).
3. `mi-<your-name>.gauth` file from admin (check your email).
4. Your 4-digit vpn `pin` (check your email).

### Setup (osx):

1. Clone the repo.
2. In the repo root folder create a `.env` file and a `ovpn-creds.txt` like the according example files.
3. Put the secret from `mi-<your-name>.gauth` to `.env` file.
4. Put your `login`, `<4-digid pin><123456>` to `ovpn-creds.txt`.
5. Open `mi-<your-name>.ovpn` via text editor and put the pass to your `ovpn-creds.txt` file to the `auth-user-pass` line (`auth-user-pass /Users/.../<path-to>/.../ovpn-creds.txt`).
6. In the terminal go to the repo root folder and execute `docker-compose build` and then `docker-compose up`. 
7. Go to [pritunl](https://client.pritunl.com/#install), download the client.
8. Run the client. Drag and drop your `mi-<your-name>.ovpn` file to it.
9. Press `menu` (burger icon) => `connect`.

You also can run `docker-compose up -d` instead of `docker-compose up` for detached behavior.

Enjoy!
