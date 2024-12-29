import re
from datetime import datetime


def update_widget_urls(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Улучшенный паттерн для захвата URL и существующих параметров timestamp
    widget_pattern = r'(https://github-profile-summary-cards\.vercel\.app/api/cards/(?:profile-details|most-commit-language|stats)\?username=MorozkoArt&theme=github_dark)(?:&timestamp=\d+\.?\d*)?'

    def replace_widget_url(match):
        timestamp = datetime.now().timestamp()
        base_url = match.group(1) # Группа 1 - URL без параметров
        return f"{base_url}&timestamp={timestamp}"

    updated_content, num_subs = re.subn(widget_pattern, replace_widget_url, content)
    print(f"Number of substitutions: {num_subs}")


    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)


if __name__ == "__main__":
    readme_path = 'README.md'
    update_widget_urls(readme_path)
    print("README.md file updated")