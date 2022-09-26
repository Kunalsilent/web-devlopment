import mongoose, { model } from "mongoose"

const VideoSchema = new mongoose.Schema({
    userId: {
        type: String,
        required: true,
    },
    videoId:{
        type: String,
         required: true,
    },
    desc: {
        type: String,
        required: true,
    
    },
    video Url: {
        type: String,
        required: true,
    },
    views: {
        type: Number,
        default: 0
    },
    tags: {
        type: [String],
        default:[],
    },
    likes:{
        type:[string],
        default:[],
    },
    dislikes:{
        typeof:[string],
        default:[],
    },
},
    { timestamps: true }
);



export default mongoose.model("video", VideoSchema);