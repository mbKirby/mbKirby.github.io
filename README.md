# CS 499 Capstone Project
## by Matthew Kirby

Welcome to my CS 499 Capstone Project GitHub Page. This portfolio showcases my skills and projects developed as part of my Computer Science program.

---

### Table of Contents
1. [Professional Self-Assessment](#professional-self-assessment)
2. [Code Review](#code-review)
3. [Software Design and Engineering Artifact](#software-design-and-engineering-artifact)
4. [Algorithms and Data Structure Artifact](#algorithms-and-data-structure-artifact)
5. [Databases Artifact](#databases-artifact)
6. [Contact Information](#contact-information)

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

---

## Software Design and Engineering Artifact
### Overview
In the Software Design and Engineering section, I showcase my ability to develop and enhance software applications, focusing on the Inventory Manager App. This project demonstrates my skills in object-oriented design, UI/UX design, and data handling. Enhancements include the implementation of a sophisticated notification system and a feature for generating and exporting reports, highlighting my adaptability and technical prowess in software engineering.


### Source Code
### Overview
In this section, I highlight my capability in software design and engineering with a focus on the Inventory Manager App. Below are key code snippets that demonstrate my proficiency in advanced features like notification systems and report generation. *Please visit my [GitHub repository](https://github.com/mbKirby/MatthewKirbyInventory/tree/master) for the complete code.*

This snippet from the Inventory Manager App demonstrates an advanced implementation of Firebase Cloud Messaging (FCM). It showcases my ability to handle incoming notifications and data payloads effectively. This feature enhances the app's interactivity and responsiveness, providing real-time updates to users, which is crucial in modern application development.
```
   public void onMessageReceived(@NonNull RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
        Log.d("FCM", "From: " + remoteMessage.getFrom());

        // Check if message contains a data payload.
        if (remoteMessage.getData().size() > 0) {
            Log.d("FCM", "Message data payload: " + remoteMessage.getData());
        }

        // Check if message contains a notification payload.
        if (remoteMessage.getNotification() != null) {
            Log.d("FCM", "Message Notification Body: " + remoteMessage.getNotification().getBody());
            // Handle notification
        }
        if (remoteMessage.getNotification() != null) {
            String title = remoteMessage.getNotification().getTitle();
            String body = remoteMessage.getNotification().getBody();
            // Call a method to display the notification
            displayNotification(title, body);
        }
    }
```
Here, I've implemented a method to save user preferences for data export formats using Android's SharedPreferences. This snippet highlights my understanding of user-centric design principles and my ability to provide customizable experiences in applications.
```
 private void saveExportPreference() {
        Spinner spinnerExportFormat = findViewById(R.id.spinnerExportFormat);
        String selectedFormat = spinnerExportFormat.getSelectedItem().toString();

        SharedPreferences preferences = getSharedPreferences("AppPreferences", MODE_PRIVATE);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString("ExportFormat", selectedFormat);
        editor.apply();
    }
```
This code demonstrates my proficiency in generating PDF reports, a vital feature for business applications. It reflects my skills in working with file systems and external libraries, showcasing a practical application of software engineering concepts.
```
private void exportAsPDF(List<Item> data) {
        File directory = context.getExternalFilesDir(null);
        File exportDir = new File(directory, "MyAppExports");
        if (!exportDir.exists()) {
            exportDir.mkdirs();
        }

        File file = new File(exportDir, "inventory.pdf");

        try {
            PdfWriter writer = new PdfWriter(file);
            PdfDocument pdf = new PdfDocument(writer);
            Document document = new Document(pdf);

            for (Item item : data) {
                document.add(new Paragraph("ID: " + item.getId()));
                document.add(new Paragraph("Name: " + item.getItemName()));
                document.add(new Paragraph("Quantity: " + item.getQuantity()));
                document.add(new Paragraph("Description: " + item.getDescription()));
                document.add(new Paragraph("\n")); // New Line
            }

            document.close();
            Toast.makeText(context, "PDF Exported Successfully", Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(context, "Error in PDF Export", Toast.LENGTH_SHORT).show();
        }
    }
```

### Narrative
For a detailed journey of my enhancements and challenges in the Inventory Manager App, read my narrative here.

---

## Algorithms and Data Structure Artifact
### Overview
The Algorithms and Data Structure section highlights my expertise in algorithmic problem-solving and data manipulation, showcased through the integration of a quicksort algorithm into the Inventory Manager App. This enhancement underlines my proficiency in applying algorithmic principles and optimizing data structures for efficient inventory management. [View the complete source code on GitHub](https://github.com/mbKirby/MatthewKirbyInventory/tree/master)



### Source Code
Here, I showcase my expertise in algorithmic thinking and data structure manipulation through the integration of the QuickSort algorithm in the Inventory Manager App. The following snippets demonstrate my skill in efficiently sorting and managing data.
This snippet illustrates my ability to implement and optimize a crucial part of the QuickSort algorithm: the partitioning process. It highlights my understanding of algorithms and efficient data manipulation, a key skill in software development.
```
private int partition(List<Item> items, int low, int high, SortCriteria criteria, SortOrder order) {
        // Random pivot selection to improve performance
        int pivotIndex = new Random().nextInt(high - low) + low;
        Item pivot = items.get(pivotIndex);
        swap(items, pivotIndex, high);

        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (compare(items.get(j), pivot, criteria, order) <= 0) {
                i++;
                swap(items, i, j);
            }
        }
        swap(items, i + 1, high);
        return i + 1;
    }
```
In this snippet, I demonstrate how to integrate the QuickSort algorithm into a functional component of my application. This reflects not only my algorithmic knowledge but also my capability to apply these concepts in a practical, user-facing scenario.
```
private void performSort(String selectedOption, boolean isAscendingOrder) {
        List<Item> allItems = itemDatabaseHelper.getItems(); // Fetch items from the database

        QuickSortManager.SortCriteria criteria = determineCriteria(selectedOption);
        QuickSortManager.SortOrder order = determineOrder(isAscendingOrder);

        quickSortManager.quickSort(allItems, criteria, order); // Perform sorting

        adapter.updateItemList(allItems); // Update the adapter with the sorted list
        adapter.notifyDataSetChanged(); // Notify the adapter to refresh the RecyclerView

    }
```

### Narrative
Discover more about my algorithmic approach and the learning curve in this project by reading my narrative here.

---

## Databases Artifact
### Overview
In the Databases section, I present my skills in database management and security through my work on the MongoDB Python Module for the Grazioso Salvare web app. This project emphasizes my ability in CRUD operations, mobile responsiveness, and secure data handling, demonstrating my comprehensive understanding of database systems and security considerations.


### Source Code
In the Databases section, I display my proficiency in database management and security through the MongoDB Python Module for the Grazioso Salvare web app. The following code excerpt exemplifies my ability in ensuring data integrity and secure handling. [View the complete source code on GitHub](https://github.com/mbKirby/CS-340-Client-Server-Development)

This code snippet showcases my attention to database security and data integrity. By implementing thorough data validation, I demonstrate my commitment to writing secure and reliable database interactions.
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
- LinkedIn: [Matthew Kirby](https://www.linkedin.com/in/matthew-kirby-a41689207/)
- GitHub: [mbKirby](https://github.com/mbKirby)
