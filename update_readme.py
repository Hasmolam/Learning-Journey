import yaml
import re

def generate_progress_bar(progress, total_blocks=10):
    filled_blocks = int(progress / 100 * total_blocks)
    empty_blocks = total_blocks - filled_blocks
    bar = '█' * filled_blocks + '░' * empty_blocks
    return f"{bar} {progress}% ✅" if progress == 100 else f"{bar} {progress}%"

def update_readme(data_file, template_file, output_file):
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"HATA: '{data_file}' dosyası bulunamadı.")
        return
    except Exception as e:
        print(f"HATA: '{data_file}' okunurken bir hata oluştu: {e}")
        return

    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"HATA: '{template_file}' dosyası bulunamadı.")
        return

    output_content = template

    if data:
        for section_key, courses in data.items():
            markdown_lines = []
            if courses:
                for course in courses:
                    progress_bar = generate_progress_bar(course.get('progress', 0))
                    name = course.get('name', 'Bilinmeyen Kurs')
                    url = course.get('url', '#')
                    markdown_lines.append(f"- [{name}]({url})  \n  İlerleme: {progress_bar}")
            value = "\n".join(markdown_lines)

            pattern = re.compile(rf"<!-- {section_key}_start -->(.*?)<!-- {section_key}_end -->", re.DOTALL)
            replacement = f"<!-- {section_key}_start -->\n{value}\n<!-- {section_key}_end -->"
            output_content = re.sub(pattern, replacement, output_content)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"'{output_file}' başarıyla güncellendi.")
    except Exception as e:
        print(f"HATA: '{output_file}' dosyası yazılırken bir hata oluştu: {e}")

if __name__ == "__main__":
    update_readme('progress.yml', 'README.template.md', 'README.md')
