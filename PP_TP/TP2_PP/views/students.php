<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des étudiants</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>

<main>
    <h1>Liste des étudiants</h1>
    <ul class="student-list"> 
    <?php foreach ($students as $student): ?>
        <li class="student-item"> 
            <span class="name"><?= htmlspecialchars($student['name']) ?></span>
            <span class="age"><?= htmlspecialchars($student['age']) ?> ans</span>
        </li>
    <?php endforeach; ?>
</ul>
</main>

</body>
</html>