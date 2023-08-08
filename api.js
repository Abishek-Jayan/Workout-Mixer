const { MongoClient, ServerApiVersion } = require("mongodb");
const dotenv = require("dotenv");
dotenv.config();
async function main() {
  const uri = "mongodb+srv://" + process.env.MONGO_URI;
  const client = new MongoClient(uri, {
    serverApi: {
      version: ServerApiVersion.v1,
      strict: true,
      deprecationErrors: true,
    },
  });
  try {
    console.log("Connecting...");
    await client.connect();
    console.log("Connected!");
    await getWorkout(client);
  } catch (e) {
    console.error(e);
  } finally {
    await client.close();
  }
}
async function getWorkout(client) {
  const database = client.db("WorkoutDatabase"); // Replace with your database name
  collection = await database.collection("Workouts");
  const document = await collection.findOne({}); // Retrieve the first document
  const chestExercises = document.chest.exercises;

  console.log("Chest Exercises:");
  chestExercises.forEach((exercise, index) => {
    console.log(`${index + 1}. ${exercise}`);
  });
}
main().catch(console.error);
