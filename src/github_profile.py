from pathlib import Path

def generate_profile(theme, **kwargs):

    with open(f'src/themes/{theme}/profile.txt') as f:
        profile = f.read()

    for key, value in kwargs.items():

        if not value:
            profile = profile.replace(f'{{ {key} }}', '')
            continue

        key_path = Path(f'src/themes/{theme}/{key}.txt')
        if not key_path.exists():
            continue

        with open(key_path) as f:
            profile_item = f.read().strip()

        profile_item = profile_item.replace('{ value }', value)
        profile = profile.replace(f'{{ {key} }}', profile_item)

    return profile

