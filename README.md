# UnHide

**UnHide** is a subdomain finder tool that retrieves information using [crt.sh](https://crt.sh/).

---

## Features

- Quickly find subdomains for a given domain.
- Fetches data directly from crt.sh.
- Outputs results to a specified file.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/und3rgr04nd/UnHide
   ```

2. Navigate to the project directory:

   ```bash
   cd UnHide
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

---

## Usage

Run the tool with the following command:

```bash
python unhide.py -d <domain> -s <output_file>
```

### Arguments:

- `-d`: Specify the target domain (e.g., `example.com`).
- `-s`: Specify the output file to save the results (e.g., `example.txt`).

### Example:

```bash
python unhide.py -d example.com -s example.txt
```

This command will find subdomains for `example.com` and save them to `example.txt`.

---

## Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`

---

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and ensure you have permission to test the target domain.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

---

## Contact

For any issues or inquiries, please reach out to the repository owner.
