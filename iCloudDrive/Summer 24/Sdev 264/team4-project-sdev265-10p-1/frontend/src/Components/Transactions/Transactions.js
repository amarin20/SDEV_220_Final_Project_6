import React from "react";
import styled from "styled-components";
import { InnerLayout } from "../../styles/Layouts";
import { useGlobalContext } from "../../context/globalContext";
import { dateFormat } from "../../utils/dateFormat";

function Transactions() {
    const { incomes, expenses } = useGlobalContext();

    // Combine and sort incomes and expenses by date
    const transactions = [...incomes, ...expenses]
        .sort((a, b) => new Date(a.date) - new Date(b.date))
        .reverse()
        ;

    return (
        <TransactionStyled>
            <InnerLayout>
                <h1>Transactions</h1>
                <ul>
                    {transactions.map((transaction, index) => (
                        <li key={index} className={transaction.type === 'income' ? 'income' : 'expense'}>
                            <span>{dateFormat(transaction.date)}</span>
                            <span>{transaction.type === 'income' ? 'Income' : 'Expense'}</span>
                            <span>{transaction.title}</span>
                            <span>${transaction.amount}</span>
                        </li>
                    ))}
                </ul>
            </InnerLayout>
        </TransactionStyled>
    );
}

const TransactionStyled = styled.div`
    display: flex;
    overflow: auto;

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        display: flex;
        justify-content: space-between;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
    }

    .income {
        color: green;
    }

    .expense {
        color: red;
    }
`;

export default Transactions;
