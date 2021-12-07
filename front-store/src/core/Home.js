import React, {useState, useEffect} from 'react'
import getProducts from './helper/coreapicalls'
import Base from './Base'
import "../styles.css"

function Home() {

    const [products, setProducts] = useState([])
    const [error, setError] = useState(null)

    const loadAllProducts = () => {
        getProducts().then(data => {
            if (data.error) {
                setError(data.error)
                console.log(error)
            }
            else {
                setProducts(data)
            }
        })
    }
    useEffect(() => {
        loadAllProducts()
    }, [])

    return (
        <Base title="Home Page" description="Welcome to Tshirt store">
            <h1>Home Component</h1>
            <div className="row">
                {products.map((product, index) => {
                    return (
                        <div key = {index}>
                            <h1>{ product.name }</h1>
                        </div>
                    )
                })}
            </div>
        </Base>
    )
}

export default Home
