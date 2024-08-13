# Windows Wallpaper Motivator

**Windows Wallpaper Motivator** is a Python-based application designed to enhance your productivity and motivation by setting a custom wallpaper on your Windows home screen. This app not only changes your wallpaper but also displays motivational information to keep you focused on your goals. It shows the number of days left until your target date and the number of days passed since a specific date. Additionally, it offers customization options for quotes and background images to align with your preferences.

## Customizing Your Experience

### Adding Personalized Quotes

1. **Edit `quotes.json`**:
   - Open the `quotes.json` file located in the `data` folder.
   - Add or modify quotes using the following format:
     ```json
     {
       "0": "Your custom quote here.",
       "1": "Another quote here."
     }
     ```
   - Each quote should be assigned a unique key (0, 1, 2, etc.).

2. **Save Changes**:
   - Save the `quotes.json` file after making your updates.

### Adding Background Images

1. **Place Your Images**:
   - Add your preferred background images to the `data/images` folder in your project directory.
   - Ensure that all images are in `.jpg` format (e.g., `background1.jpg`, `background2.jpg`).

## Features

- **Custom Wallpaper**: Change your Windows desktop wallpaper programmatically to any `.jpg` image you choose.
- **Motivational Countdown**: Display the number of days left until a target date and the number of days passed since a start date.
- **Custom Quotes**: Personalize your motivational experience by adding your own quotes.
- **Background Image Preferences**: Set and manage your preferred `.jpg` background images for a personalized touch.
