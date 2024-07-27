const mongoose = require('mongoose');


const IncomeSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true,
        maxLength: 50
    },
    amount: {
        type: Number,
        required: true,
        maxLength: 20,
        min:0, //ensures that the amount is not negative 
        trim: true
    },
    type: {
        type: String,
        default: "income"
    },
    date: {
        type: Date,
        required: true,
        trim: true,
        maxLength: 50 // added length for consistancy
    },
    category: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        required: true,
        maxLength: 200, //Increased maxLength for more detailed descriptions
        trim: true
    },
}, {timestamps: true})


IncomeSchema.pre('save', function(next) {
    // Sanitize the title, category, and description fields by removing $ and . characters
    // This helps prevent NoSQL injection attacks
    this.title = this.title.replace(/[$.]/g, '');
    this.category = this.category.replace(/[$.]/g, '');
    this.description = this.description.replace(/[$.]/g, '');
    next();
});


module.exports = mongoose.model('Income', IncomeSchema)