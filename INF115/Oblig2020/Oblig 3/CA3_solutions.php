<!DOCTYPE html>
<html>
    <head>
        <title>INF115 - CE3</title>
    </head>
    <body>
        <h1>INF115 - Compulsary exercise 3</h1>

            <?php
            /*
                Database configuration
            */

            // Connection parameters
            $host 		= 'localhost';
            $user 		= 'root';
            $password 	= '';
            $db 		= 'bysykkel';

            // Connect to the database
            $conn = mysqli_connect($host, $user, $password, $db);

            // Connection check
            if(!$conn) {
                exit('Error: Could not connect to the database.');
            }

            // Set the charset
            mysqli_set_charset($conn, 'utf8');
            ?>

        <h1> Task 1 </h1>
            <h2> a) </h2>
            <!-- Write your solution to 1a here -->

            <?php
            echo "<b> Elias Djupesland</b> <br>";
            echo "<b> edj001</b>";
            ?>

            <h2> b) </h2>
            <!-- Write your solution to 1b here -->
            
            <form action="?" method="post">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" required><br>
                <label for="phone">Phone number:</label><br>
                <input type="text" id="phone" name="phone" required><br>
                <label for="mail">Email:</label><br>
                <input type="text" id="mail" name="mail" required><br>
                <input type="submit" value="Submit">
                <input type="reset" value="Reset">
            </form><br>

            <?php
                if (isset($_POST['name']))
                {
                    $name = $_POST['name'];
                    $phone = $_POST['phone'];
                    $mail = $_POST['mail'];

                    echo $name;
                    echo "<br>";
                    echo $phone;
                    echo "<br>";
                    echo $mail;

                }
            ?>



            <h2> c) </h2>
            <!-- Write your solution to 1c here -->

            <?php
                if (isset($_POST['name'])) {

                    # Validating name
                    if (!preg_match('/[^A-Åa-å]+/', str_replace(' ', '', $name))){
                        echo $name . " - Valid";
                    } else {
                        echo $name . " - Not valid";
                    }

                    echo "<br>";

                    #Validating phone
                    if (is_numeric($phone) and strlen($phone)==8) {
                        echo $phone . " - Valid";
                    } else {
                        echo $phone . " - Not valid";
                    }

                    echo "<br>";

                    #Validating email
                    if (strpos($mail, '@')) {
                        echo $mail . " - Valid";
                    } else {
                        echo $mail . " - Not valid";
                    }
                }
    
            ?>
            

        <h1> Task 2 </h1>
            <h2> a) </h2>
            <!-- Write your solution to 2a here -->

            <?php
            $sql = "SELECT name FROM users ORDER BY name";
            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>Name</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['name'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>

            <h2> b) </h2>
            <!-- Write your solution to 2b here -->

            <?php
            $sql = "SELECT DISTINCT name, status FROM bikes";
            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>Bike name</th>
            <th>Status</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['name'] . "</td>";
                echo "<td>" . $row['status'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>

            <h2> c) </h2>
            <!-- Write your solution to 2c here -->

            <?php
            $sql = "SELECT `TABLE_NAME`, `TABLE_ROWS`
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_TYPE = 'BASE TABLE' 
                    AND TABLE_SCHEMA='bysykkel'";

            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>Table name</th>
            <th>Rows</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['TABLE_NAME'] . "</td>";
                echo "<td>" . $row['TABLE_ROWS'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>

        <h1> Task 3 </h1>
            <h2> a) </h2>
            <!-- Write your solution to 3a here -->

            <?php
            $sql = "Select `TABLE_NAME`, GROUP_CONCAT(`COLUMN_NAME`) From INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'bysykkel' GROUP BY `TABLE_NAME`";
            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>Table</th>
            <th>Attributes</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['TABLE_NAME'] . "</td>";
                echo "<td>" . $row['GROUP_CONCAT(`COLUMN_NAME`)'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>

            <h2> b) </h2>
            <!-- Write your solution to 3b here -->
			 <?php
            $sql = "SELECT S.station_id, S.name, COUNT(T.trip_id) AS \"Trips\" FROM trips AS T, stations as S WHERE T.end_station = S.station_id GROUP BY S.name";
            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>Station ID</th>
            <th>Station name</th>
            <th>Number of trips</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['station_id'] . "</td>";
                echo "<td>" . $row['name'] . "</td>";
                echo "<td>" . $row['Trips'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>

            <h2> c) </h2>
            <!-- Write your solution to 3c here -->

            <?php
            $sql = "SELECT users.user_id, users.name,
            count(case year(subscriptions.start_time) when 2018 then 1 else null end) as '2018',
            count(case year(subscriptions.start_time) when 2019 then 1 else null end) as '2019',
            count(case year(subscriptions.start_time) when 2020 then 1 else null end) as '2020',
            count(case year(subscriptions.start_time) when 2021 then 1 else null end) as '2021'
            FROM `users` INNER JOIN subscriptions on users.user_id = subscriptions.user_id GROUP BY users.user_id";
            $result = $conn->query($sql);

            echo "<table border='1'>
            <tr>
            <th>user_id</th>
            <th>Name</th>
            <th>2018</th>
            <th>2019</th>
            <th>2020</th>
            <th>2021</th>
            </tr>";

            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['user_id'] . "</td>";
                echo "<td>" . $row['name'] . "</td>";
                echo "<td>" . $row['2018'] . "</td>";
                echo "<td>" . $row['2019'] . "</td>";
                echo "<td>" . $row['2020'] . "</td>";
                echo "<td>" . $row['2021'] . "</td>";
                echo "</tr>";
            }

            echo "</table>";
            ?>
        
        <h1> Task 4 </h1>
        <!-- Write your solution to 4 here -->

        <form action="?", method="POST">
            <label for="station">Choose a station:</label>
            <select name="station" id="station">
                <option value=1>Høyteknologisenteret</option>
                <option value=2>Nygårdsporten</option>
                <option value=3>Festplassen</option>
                <option value=4>Småstrandgaten</option>
                <option value=5>Torgallmenningen</option>
            </select>
            <input type="submit" value="Submit">
        </form>

        <br>

        
        
        <?php
            if (isset($_POST['station'])) {
                $station_id = $_POST['station'];
                $sql = "SELECT * FROM stations WHERE station_id = $station_id";

                $result = $conn->query($sql);

                echo "<table border='1'>
                <tr>
                <th>Name</th>
                <th>Availability</th> 
                <th>Location</th>
                </tr>";

                while($row = $result->fetch_assoc()) {
                    $avail_perc = round(intval($row['available_spots']) / intval($row['max_spots']),2)*100;
                    echo "<tr>";
                    echo "<td>" . $row['name'] . "</td>";
                    echo "<td>" . $avail_perc. "%</td>";
                    echo "<td> <a href=" . "https://www.google.com/maps?q=" . $row['latitude'] . "," . $row['longitude'] . " target='_blank'>Link</a> </td>";
                    echo "</tr>";
                }

                echo "</table>";
            }
        ?>
        <br>
    </body>
</html>