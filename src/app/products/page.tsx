'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { format } from 'date-fns';
import axios from "axios";

export default function ProductForm() {
    const router = useRouter();
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const [formData, setFormData] = useState({
        name: '',
        size: '',
        description: '',
        category: '',
        quantity_in_carton: '',
        price: '',
        image_url: '',
        user_id: '',
    });
    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
    ...prev,
    [name]: value
    }));
    };

    const handleDocumentChange = (index: number, e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    const updatedDocuments = [...formData.documents];
    updatedDocuments[index] = {
    ...updatedDocuments[index],
    [name]: value
    };
    setFormData(prev => ({
    ...prev,
    documents: updatedDocuments
    }));
    };
    const addDocument = () => {
    setFormData(prev => ({
    ...prev,
    documents: [
        ...prev.documents,
        {
        document_type: '',
        file_path: ''
        }
    ]
    }));
    };
    const removeDocument = (index: number) => {
    const updatedDocuments = [...formData.documents];
    updatedDocuments.splice(index, 1);
    setFormData(prev => ({
    ...prev,
    documents: updatedDocuments
    }));
    };

    const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>, fieldName: string) => {
    const file = e.target.files?.[0];
    if (!file) return;

    try {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post("http://localhost:8000/uploadfile/", formData, {
        headers: {
        'Content-Type': 'multipart/form-data'
        }
    });
}