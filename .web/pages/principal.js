/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Box, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Box sx={{"bg": "#292833", "backgroundSize": "cover", "height": "100vh"}}>
  <Box sx={{"bg": "#FF5C00", "border": "1px solid #000"}}>
  <HStack>
  <Link as={NextLink} href={`principal`}>
  <HStack>
  <Heading size={`lg`} sx={{"color": "#000000"}}>
  {`Game`}
</Heading>
  <Heading size={`lg`} sx={{"color": "#FFFFFF"}}>
  {`Mini`}
</Heading>
  <Heading size={`lg`} sx={{"color": "#FFFFFF"}}>
  {`⭐`}
</Heading>
</HStack>
</Link>
  <Spacer/>
  <Link as={NextLink} href={`https://github.com/santyjL/santyjL`} isExternal={true}>
  <ChakraImage src={`/github icon.png`} sx={{"width": "3.6em", "height": "100%"}}/>
</Link>
</HStack>
</Box>
  <Center>
  <Box sx={{"borderRadius": "0.9em", "background": "#32135A", "margin": "3em", "PADDINGX": "0.6em", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "40%"}}>
  <Center>
  <Heading sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`Mini Juegos disponibles`}
</Heading>
</Center>
</Box>
</Center>
  <Box sx={{"width": "100%", "marginY": "1em"}}>
  <Center sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "3em", "PADDINGX": "0.6em", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00"}}>
  <VStack>
  <HStack>
  <Link as={NextLink} href={`reglas_juego_uno`}>
  <Heading sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖`}
</Heading>
</Link>
</HStack>
  <HStack>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em", "marginX": "1.5em", "marginY": "1em"}}>
  {`El clasico juego de pieda papel o tijeras  lo conocemos todo el mundo pero no todos conocen el juego de piedra, papel, tijeras, gallina, spock`}
</Text>
</HStack>
</VStack>
</Center>
</Box>
  <Box>
  <Center>
  <HStack sx={{"width": "97%"}}>
  <Center>
  <VStack sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "PADDINGX": "0.6em", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "50%"}}>
  <HStack>
  <Link as={NextLink} href={`Encuentra_el_numero`}>
  <Heading sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`Encuentra el numero 🎲`}
</Heading>
</Link>
</HStack>
  <HStack>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em", "marginX": "1.5em", "marginY": "1em"}}>
  {`del 1 al 100 se a perdido un numero pero cual sera, hay que entcontrarlo`}
</Text>
</HStack>
</VStack>
  <Spacer/>
  <Center sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "PADDINGX": "0.6em", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "50%"}}>
  <VStack>
  <HStack>
  <Link as={NextLink} href={`3_en_rayas`}>
  <Heading sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`Tres en raya ❌ | ⭕  `}
</Heading>
</Link>
</HStack>
  <HStack>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em", "marginX": "1.5em", "marginY": "1em"}}>
  {`El clasico “Tres en raya no podia faltar  un juego mitico que todos conocemos`}
</Text>
</HStack>
</VStack>
</Center>
</Center>
</HStack>
</Center>
</Box>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}