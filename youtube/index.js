import express from "express"
import mongoose from "mongoose"
import dotenv from "dotenv"
import userRoutes from "./rotes/users.js"

const app =express()
dotenv.config()

const connect=() =>{
    mongoose
    .connect(process.env.MONGO)
    .then(()=>{
        console.log("connect to DB");
    })
    .catch((err) =>{
        throw err;
    });
};

app.use("/api/users", userRouters)

app.listen(8800,()=>{
    connect()
    console.log("connected to server")
});