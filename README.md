# CS 499 Capstone Project
## by Matthew Kirby

Welcome to my CS 499 Capstone Project GitHub Page. This portfolio showcases my skills and projects developed as part of my Computer Science program.

---

### Table of Contents
1. [Professional Self-Assessment](#professional-self-assessment)
2. [Software Design and Engineering Artifact](#software-design-and-engineering-artifact)
3. [Algorithms and Data Structure Artifact](#algorithms-and-data-structure-artifact)
4. [Databases Artifact](#databases-artifact)
5. [Contact Information](#contact-information)

---

## Professional Self-Assessment
As I reflect on my journey through the Computer Science program at SNHU, I realize how significantly my coursework and the development of my ePortfolio have shaped my professional trajectory. My initial interest in backend development evolved, leading me to a profound appreciation for front-end development and UI design. This shift is not just a change in interest but a testament to the program's influence in expanding my perspective and skills. My projects in CS 360 Mobile Architect Programming and MongoDB Python module showcase my adaptability and technical skills.

Collaboration and Communication :
My project on the Inventory Manager App, as part of CS 360 Mobile Architect Programming, is a prime example of my growth in collaborative environments and communication. By enhancing the notification system I’ve improved communication with the users which has shown my ability to design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts. Additionally, implementing the report generation and data export features required me to think critically about user needs and preferences, which allowed me to employ strategies for building collaborative environments that enable diverse audiences to support organizational decision-making in computer science. Overall, this process improved my ability to engage with diverse audiences and communicate complex technical information easily.

Algorithms and Data Structures :
The implementation of a quicksort algorithm in the Inventory Management app was a direct application of algorithmic principles. This enhancement displays my ability to design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices.

Innovative Techniques and Tools :
My work on the MongoDB Python Module for the Grazioso Salvare web app demonstrates my proficiency using innovative techniques and tools. By integrating CRUD operations through a form and enhancing mobile responsiveness. These actions showcase my ability to use well-founded and innovative techniques, skills, and tools in computing practices to implement computer solutions that deliver value and accomplish industry-specific goals.
Security Mindset :
Throughout the program, I’ve developed a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. For example, for my MongoDB Python project, I integrated essential validation and sanitization methods for POST requests, ensuring robust defense against data manipulation and injection attacks. Additionally, I’ve ensured that database connections and environmental variables are stored in their file and are not publicly available. In addition, I worked on a project for CS-465 where I developed a user registration and login system, incorporating JWT tokens to validate user sessions. These and many other instances in my time at SNHU have reinforced a security mindset.
Integrating Artifacts and Skills:
Each of these projects and enhancements has contributed to a cohesive narrative of my abilities and growth in the field of computer science. The Inventory Manager App and MongoDB Python Module showcase my front-end development and user interface design skills as well as highlight my backend development capabilities and my understanding of database security.
In conclusion, my ePortfolio is a comprehensive showcase of my skills and learning journey in the Computer Science program. It reflects not only my technical abilities but also my adaptability, problem-solving skills, and commitment to continuous learning and improvement. As I step into the professional world, I am confident in my ability to contribute effectively and innovatively in various roles within the computer science field.


---

### Code Review

## Software Design and Engineering Artifact
### Overview
In the Software Design and Engineering section, I showcase my ability to develop and enhance software applications, focusing on the Inventory Manager App. This project demonstrates my skills in object-oriented design, UI/UX design, and data handling. Enhancements include the implementation of a sophisticated notification system and a feature for generating and exporting reports, highlighting my adaptability and technical prowess in software engineering.


### Source Code
https://github.com/mbKirby/MatthewKirbyInventory/tree/master

### Narrative
For a detailed journey of my enhancements and challenges in the Inventory Manager App, read my narrative here.

---

## Algorithms and Data Structure Artifact
### Overview
The Algorithms and Data Structure section highlights my expertise in algorithmic problem-solving and data manipulation, showcased through the integration of a quicksort algorithm into the Inventory Manager App. This enhancement underlines my proficiency in applying algorithmic principles and optimizing data structures for efficient inventory management.


### Source Code


### Narrative
Discover more about my algorithmic approach and the learning curve in this project by reading my narrative here.

---

## Databases Artifact
### Overview
In the Databases section, I present my skills in database management and security through my work on the MongoDB Python Module for the Grazioso Salvare web app. This project emphasizes my ability in CRUD operations, mobile responsiveness, and secure data handling, demonstrating my comprehensive understanding of database systems and security considerations.


### Source Code
https://github.com/mbKirby/CS-340-Client-Server-Development

```
def _validate_data(self, data):
        # Basic validation checks on the data
        if not data:
            raise ValueError("Data is empty")
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        required_fields = ['animal_id', 'animal_type', 'breed', 'color', 'date_of_birth', 'sex_upon_outcome']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Required field '{field}' is missing")
```

### Narrative
Learn about my journey in database management and the enhancements I made by reading my narrative here.

---

## Contact Information
- Email: [matthew.kirby90@yahoo.com](mailto:matthew.kirby90@yahoo.com)
- LinkedIn: [Matthew Kirby](https://www.linkedin.com/in/matthew-kirby-a41689207/)
- GitHub: [mbKirby](https://github.com/mbKirby)
