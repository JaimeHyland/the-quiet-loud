# The Quiet Loud

A "With Heart" hackathon project: a web app that helps users name an emotion from their input and receive a supporitve and human-centered response.

# User Experience

## Types of Users
- Neurodivergents who may need help identifying and naming emotions
- Users who would like support understanding and reflecting on their emotions

## User Stories
- As a user, I should be able to input text describing how I feel
- As a user, I should receive an emotion prediction and supportive response
- As a user, I should be able to navigate easily to different areas of the site

## User Flow
1. User logs in
2. User enters a sentence/paragraph describing how they feel
3. App returns:
    - predicted emotion (joy/sadness/anger/fear/love/surprise)
    - supportive reframe

# Design
We chose a calming colour palette to help users feel safe and supported while interacting with the app.

## Colour Scheme
Soft neutrals keep the space gentle and welcoming, while the darker tones provide grounding and clarity. Together, the palette reflects the app’s purpose: creating an environment where users can slow down, breathe, and be honest with themselves.

The colour palette was generated using the online tool [Coolors](https://coolors.co/c9a96e-f7f2eb-ede5d8-a89e92-6b6158-1e1c1a).

![Colour Palette](documentation/images/colour_scheme.png)

## Typography

### Font Choices:

#### Cormorant Garamond: used for headings. 
This elegant serif font is inspired by classic Garamond typefaces. It adds sophistication and a calm, reflective tone, making it ideal for creating a welcoming, thoughtful atmosphere in a mood-focused app. Its delicate curves and high contrast make headings feel distinctive and readable.

Sample from the [Google Fonts](https://fonts.google.com/specimen/Cormorant+Garamond) website:

![Cormorant Garamond](documentation/images/cormorant-garamond.png)

#### DM Sans: used for body text. 
This modern sans-serif font is geometric, clean, and highly legible. It pairs well with a serif heading by providing clarity and accessibility for longer passages of text. DM Sans helps users focus on content without distraction, maintaining a smooth reading experience across devices.

Together, these fonts create a balanced and approachable style, giving the app a professional yet gentle feel, perfectly suited to encouraging users to reflect on their mood and wellbeing.

Sample from the [Google Fonts](https://fonts.google.com/specimen/DM+Sans) website:

![DM Sans](documentation/images/dm-sans-font.png)

Additionally, [Font Awesome](https://fontawesome.com/) icons were used throughout the site to keep the interface clean, consistent, and visually intuitive.

## Wireframes

Wireframes were created using Figma - the industry top wireframing software.

| Page | Wireframe |
| --- | --- |
| Homepage | ![Homepage](documentation/images/frame-1.png) |
| Today | ![Today](documentation/images/frame-2.png) |
| Journey | ![Journey](documentation/images/frame-3.png) |
| Support | ![Support](documentation/images/frame-4.png) |

# Features

## Current Features
- User input page
- Emotion prediction response
- Supportive reframe generation
- User authentication and saved history

## Future Features
- Emotion summary or insights
- Emotion trends or summary visualisation

# Responsiveness
...

# Testing

# Technologies and Languages

## Languages
- HTML5 - to structure the project
- CSS3 - to style HTML elements
- Javascript - for an interactive experience
- Python - for backend developement

## Frameworks, Librariers & Tools
- Django - python framework and auth
- Machine Learning model - emotion classification model trained on emotion dataset (see credits)
- Git - version control
- Github - development workflow

# Deployment
1. Navigate to the repository
2. Click on settings in the tabs
3. Click on pages in the left hand sidebar
4. In the source dropdown, select Deploy from a branch
5. Select Main as the branch
6. Click the save button next to main and root

## Creating a Fork
1. Navigate to the repository
2. In the top right, click on the arrow next to the fork button
3. Select create new fork
4. Copy the main branch
5. Click create a fork button
6. A new repository will appear in your Github account

## Cloning a Repository
1. Navigate to the respository
2. Click on the green code button near the top of the repository
3. Copy the link
4. Opena new terminal and change into the directory you wish to clone the repository to
5. Type git clone and then paste the link
6. Press enter to create your local clone

# Credits
- Kaggle dataset for machine learning (https://www.kaggle.com/datasets/kushagra3204/sentiment-and-emotion-analysis-dataset)