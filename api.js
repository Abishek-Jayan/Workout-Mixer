const { MongoClient, ServerApiVersion } = require("mongodb");
const dotenv = require("dotenv");
const express = require("express");

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;
const uri = "mongodb+srv://" + process.env.MONGO_URI;
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

app.get("/getWorkoutData", async (req, res) => {
  try {
    console.log("Connecting...");
    await client.connect();
    console.log("Connected!");
  } catch (e) {
    console.error(e);
  }
  data = req.query;
  workout = await getWorkout(client, data.musclegroup);
  res.json(workout);
});

async function getWorkout(client, _musclegroup) {
  const database = client.db("WorkoutDatabase");
  collection = await database.collection("Workouts");
  query = {
    [_musclegroup]: { $exists: true },
  };
  const document = await collection.findOne(query);
  const exercises = document[_musclegroup].exercises;
  await client.close();
  return exercises;
}
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
