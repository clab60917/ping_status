
# Ping Status Tool

![Ping Status](https://img.shields.io/badge/Ping-Status-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

Ping Status Tool is a simple but effective Python script that allows you to quickly check the status of multiple IP addresses from a file. It displays the "UP" and "DOWN" hosts in a colorful, well-structured table, with a progress bar showing the ping advancement.

## Features
- 🟢 Displays accessible hosts (UP) in green.
- 🔴 Displays inaccessible hosts (DOWN) in red.
- 🔄 Progress bar showing the status of IP pings.
- 📄 Takes as input a file containing a list of IP addresses to ping.

## Installation

### 1. Clone the project
Start by cloning the GitHub repository to your local machine.

```bash
git clone https://github.com/clab60917/ping_status.git
cd ping_status
```

### 2. Make the script executable

Before using the tool, you need to make the script executable:

```bash
chmod +x ping_status.py
```

### 3. Add to your PATH (Optional)

To run the script from anywhere, you can add it to your `PATH` or move it to `/usr/local/bin/`:

```bash
sudo mv ping_status.py /usr/local/bin/
```

## Usage

The tool is easy to use. It takes a text file as an argument containing the list of IP addresses to ping.

```bash
./ping_status.py /path/to/target.txt
```

### Example

If your `target.txt` file contains the following IP addresses:

```
192.168.1.1
8.8.8.8
1.1.1.1
```

Run the following command:

```bash
./ping_status.py target.txt
```

The output will look like this:

```
Pinging IPs: 100%|██████████████████████████| 3/3 [00:03<00:00, 1.00ip/s]

UP                   | DOWN                 
----------------------------------------
8.8.8.8              | 192.168.1.1          
1.1.1.1              |                      
----------------------------------------
```

## Dependencies

This project uses a few external Python libraries. Install them using `pip` if they are not already available on your system:

```bash
pip install termcolor tqdm
```

### Main Libraries
- `subprocess`: to execute the `ping` command.
- `termcolor`: to colorize the IP addresses in the terminal.
- `tqdm`: to display the progress bar.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

_Developed with ❤️ by [clab60917](https://github.com/your_username)_
