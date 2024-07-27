const { body, validationResult} = require('express-validator')
const ExpenseSchema = require("../models/ExpenseModel")

// New validation/Sanitzation using Express validator
// I didnt wanna remove any of the old code. I commented it out for now

exports.addExpense = [
    body('title')
        .notEmpty().withMessage('title is required ')
        .isLength({max:50}).withMessage('title must be less than 50 characters')
        .escape().trim(),
    body('amount')
        .isFloat({gt:0}).withMessage('Amount must be a postive number'),
    body('category')
        .notEmpty().withMessage('category is required')
        .isLength({max:50}).withMessage('categoty must be less than 50 characters')
        .escape().trim(),
    body('description')
        .notEmpty().withMessage('date is required')
        .isLength({max:200}).withMessage('description must be less than 200 characters')
        .escape().trim(),
    body('date')
    .notEmpty().withMessage('date is required')
    .isISO8601().withMessage('date must be a valid date')
    .toDate(),

    async (req,res) => {
        const errors = validationResult(req);
        if(!errors.isEmpty()){
            return res.status(400).json({errors: errors.array()});
        }
    

    const { title, amount, category, description, date} = req.body;

    const expense = new ExpenseSchema({
        title,
        amount,
        category,
        description,
        date,
    });


    try{
        await expense.save();
        res.status(200).json({message: 'Expense Added'});
    } catch (error){
        res.status(500).json({message: 'Server Error'});
    }

    console.log(expense);
    }
];






// exports.addExpense = async (req, res) => {
//     const {title, amount, category, description, date} = req.body

//     const expense = ExpenseSchema({
//         title, 
//         amount, 
//         category,
//         description,
//         date
//     })

//     try {
//         //validations
//         if(!title || !category || !description || !date){
//             return res.status(400).json({message: 'All fields are required'})
//         }
//         if(amount <=0 || !amount === 'number' ){
//             return res.status(400).json({message: 'Amount must be a positive number'})
//         }
//         await expense.save()
//         res.status(200).json({message: 'Expense Added'})
//     } catch (error) {
//         res.status(500).json({message: 'Server Error'})
        
//     }
//     console.log(expense)
// }

exports.getExpenses = async (req, res) => {
    try {
        const expenses = await ExpenseSchema.find().sort({createdAt: -1})
        res.status(200).json(expenses)
    } catch (error) {
        res.status(500).json({message: 'Server Error'})
    }
}

// I updated the function to add error messeage in case it cant find 
exports.deleteExpense = async(req, res) => {
    const{ id } = req.params;
    try{
        const expense = await ExpenseSchema.findByIDAndDelete(id);
        if (!expense){
            return res.status(400).json({message: 'expesnse not found'});
        }
        res.status(200).json({message: 'Expense Deleted'});
    } catch (err){
        res.status(500).json({ message: 'Server Error'});
    }
};






// exports.deleteExpense = async (req, res) => {
//     const {id} = req.params;
//     ExpenseSchema.findByIdAndDelete(id)
//         .then((expense) => {
//             res.status(200).json({message: 'Expense Deleted'})
//         })
//         .catch ((err) =>{
//             res.status(500).json({message: 'Server Error'})
//         })
// }