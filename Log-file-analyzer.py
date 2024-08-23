import re
from collections import Counter

def analyze_log_file(log_file):
    with open(log_file, 'r') as f:
        logs = f.readlines()

    error_pattern = re.compile(r'404')
    page_pattern = re.compile(r'"GET (.*?) HTTP')
    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    error_count = 0
    pages = []
    ip_addresses = []

    for log in logs:
        if error_pattern.search(log):
            error_count += 1
        page_match = page_pattern.search(log)
        if page_match:
            pages.append(page_match.group(1))
        ip_match = ip_pattern.search(log)
        if ip_match:
            ip_addresses.append(ip_match.group(1))


    page_counts = Counter(pages).most_common(5)
    ip_counts = Counter(ip_addresses).most_common(5)


    report = f"Total 404: {error_count}\n"
    report += "Most Requested:\n"
    for page, count in page_counts:
        report += f"  {page}: {count} requests\n"
    report += "IP Addresses Most Requests:\n"
    for ip, count in ip_counts:
        report += f"  {ip}: {count} requests\n"
    return report

log_file = "/home/elite/webserver.log"
report = analyze_log_file(log_file)
print(report)
