'use client';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { format } from 'date-fns';

export default function ProductForm() {
    const router = useRouter();
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [error, setError] = useState(null);


    const [formData, setFormData] = useState({
        name:'',
        size:'',
        description:'',
        category:'',
        quantity_in_carton:'',
        price:'',
        image_url:'',
        id: '',
    });

}