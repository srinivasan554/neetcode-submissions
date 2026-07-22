class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string_list = []

        for s in strs:
            encoded_string_list.append(f"{len(s)}#{s}")

        return "".join(encoded_string_list)

    def decode(self, s: str) -> List[str]:

        i = 0

        decoded_strings_list = []


        while i < len(s):

            j = i

            while (s[j] != '#'):
                j += 1

            length_of_string = int(s[i:j])

            start_of_string = j+1

            end_of_string = start_of_string + length_of_string

            decoded_strings_list.append(s[start_of_string:end_of_string])

            i = end_of_string
        
        return decoded_strings_list
