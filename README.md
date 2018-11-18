# Autofill text with a 2FA code for use in VPN

In order to use this repo, you just need [docker](https://www.docker.com/get-started).

Create a .env file and a ovpn-creds.txt like the according example files.

Then, run the following 2 commands:

```bash
docker-compose build
docker-compose up
```

(Or `docker-compose up -d` for detached behavior)

This repo will then automatically replace the last 6 characters of your ovpn-creds.txt file.

If your ovpn configuration is set to look to this file for credentials, you're all set!

The line needed for the above within the .ovpn file is: `auth-user-pass /Users/.../ovpn-creds.txt`. Of course, you need to have the file within the same folder.

Favorite vpn client for the above setup is [pritunl](https://client.pritunl.com/#install)
