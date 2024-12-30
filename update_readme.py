import re
from datetime import datetime

def update_readme(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Обновление timestamp в URL виджетов
    widget_pattern = r'(https://github-profile-summary-cards\.vercel\.app/api/cards/(?:profile-details|most-commit-language|stats)\?username=MorozkoArt&theme=github_dark)(?:&timestamp=\d+\.?\d*)?'

    def replace_widget_url(match):
        timestamp = datetime.now().timestamp()
        base_url = match.group(1)
        return f"{base_url}&timestamp={timestamp}"

    updated_content, num_subs = re.subn(widget_pattern, replace_widget_url, content)
    print(f"Number of widget substitutions: {num_subs}")

    # Обновление даты последнего обновления
    date_pattern = r'### My stat \(last update: (\d{2}\.\d{2}\.\d{4}(?:\s\d{2}:\d{2}:\d{2})?)?\)'
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
    replacement = f'### My stat (last update: {formatted_date})'


    updated_content, date_subs = re.subn(date_pattern, replacement, updated_content)
    print(f"Number of date substitutions: {date_subs}")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == "__main__":
    readme_path = 'README.md'
    update_readme(readme_path)
    print("README.md file updated")