import { useAuth } from "@/contexts/auth";
import { useState } from "react";
import useSWR from 'swr'

export default function useResource() {


    const url = process.env.NEXT_PUBLIC_API_RESOURCE_URL
    const { token, logout } = useAuth();
    // const [data, setDate]= useState([]);
    const { data, error,mutate } = useSWR([url,token], fetchResource)


    function config() {
        return {
            headers: {
                 "Content-Type": "application/json",
                 "Authorization":"Bearer " + token.access
         },


        }
    }

    async function fetchResource() {
        if (!token) {
            return
        }
        try {
            const response = await fetch(url, config())
            const jsonResponse  = await response.json()
            // console.log(1111,jsonResponse)
            // setDate(jsonResponse)
            return jsonResponse


        } catch (error) {
            errorHandler(error)
        }

    }
    async function createResource(newLocation){

        if (!token) {
            return
        }try{

            const options =config()
            options.method ="POST"
            options.body  = JSON.stringify(newLocation)
    
            await fetch(url, options )
            mutate()

        }catch (error) {
            errorHandler(error)
        }


    }
    async function deleteResource(id){

        const deleteUrl =url+id
        if (!token) {
            return
        }try{

            const options =config()
            options.method ="DELETE"
    
            await fetch(deleteUrl, options )
            mutate()

        }catch (error) {
            errorHandler(error)
        }


    }




    function errorHandler(error) {
        console.log(error);
        logout()

    }


    return {
        response : data,
        createResource,
        deleteResource,
    }



}