<html>
    <head>
        <title>My Shop</title>
    </head>
    <body>
        <h1>La liste des produits disponibles est :</h1>
        <ul>
            <?php
            // Appel de l'API via le nom du service Docker Compose
            $json = file_get_contents('http://product-service/');
            $obj = json_decode($json);

            $products = $obj->products;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>