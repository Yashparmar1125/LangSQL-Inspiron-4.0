import express from "express";
import testTrinoConnection from "../databaseHandlers/trino.handler.js"; // Import the connection function
import axios from "axios";
import { LangflowClient } from "@datastax/langflow-client";

const router = express.Router();
// Route to check Trino connection
router.post("/testtrino", async (req, res) => {
  try {
    console.log("Received Connection Config:", req.body);

    const connectionConfig = req.body; // Extract connection details from request body

    if (
      !connectionConfig.host ||
      !connectionConfig.port ||
      !connectionConfig.user ||
      !connectionConfig.password
    ) {
      return res.status(400).json({
        success: false,
        message: "Missing required connection parameters",
      });
    }

    const result = await testTrinoConnection(connectionConfig);
    res.status(200).json(result);
  } catch (error) {
    console.error("Error in /testtrino:", error);
    res.status(500).json({
      success: false,
      message: "Internal Server Error",
      error: error.message,
    });
  }
});

router.post("/client");

export default router;
