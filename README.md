# Grazioso-Salvare-Dashboard-Project
A MongoDB + Python Dash application that filters and visualizes rescue dog data.

Writing maintainable and readable code means keeping things organized, simple, and easy to understand for both yourself and others. In this project, I achieved this by separating the database logic into a CRUD Python module and keeping the dashboard code focused on the user interface. This made the overall project easier to follow and reduced confusion when debugging.

One major advantage of using the CRUD module was that it allowed me to reuse the same database functions throughout the dashboard without rewriting queries multiple times. It also made the code more adaptable, since changes to the database connection or query logic could be made in one place. In the future, I could reuse this module in other projects that require database interaction, such as web applications, APIs, or data-driven tools.

When working on this project, I approached the problem by breaking it into smaller steps. I first focused on making sure the database was working correctly, then built the CRUD module, and finally developed the dashboard interface. After that, I connected all the components using callbacks to make the dashboard interactive.

This project was different from earlier assignments because it required combining multiple technologies instead of working on one isolated task. I had to think about how the database, backend logic, and user interface all worked together. In the future, I would continue using this structured approach by planning ahead, testing each part individually, and then integrating everything into a complete system.

Computer scientists create systems that help solve real-world problems by organizing and processing data efficiently. In this project, the dashboard allows a company like Grazioso Salvare to quickly filter and identify dogs that meet specific rescue requirements.

Without a system like this, users would have to manually search through large amounts of data, which would be time-consuming and prone to error. By building this dashboard, I helped demonstrate how technology can improve efficiency, support decision-making, and make complex data easier to understand. This shows the real-world impact of computer science in helping organizations work more effectively.
